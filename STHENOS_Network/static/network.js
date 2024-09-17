document.addEventListener('DOMContentLoaded', function() {
    const emailsvView = document.querySelector('#emails-view');
    if (emailsvView) emailsvView.style.display = 'none';
    const composeView = document.querySelector('#emails-view');
    if (composeView) composeView.style.display = 'none';

    const inboxNav = document.querySelector('#inboxNav');
    if (inboxNav) inboxNav.addEventListener('click', () => load_mailbox('inbox'));
    const sentNav = document.querySelector('#sentNav');
    if (sentNav) sentNav.addEventListener('click', () => load_mailbox('sent'));
    const composeNav = document.querySelector('#composeNav');
    if (composeNav) composeNav.addEventListener('click', () => compose_email());

    // Get CSRF token from meta tag
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    document.querySelectorAll('.like-button')?.forEach(button => {
        button.addEventListener('click', (event) => {
            const postView = event.target.closest('.text-container');
            like(postView.dataset.postid, button);
        });
    });

    document.querySelector('#compose-form-messages')?.addEventListener('submit', function(event) {
        event.preventDefault();
        sendmail();
    });

    const followButton = document.querySelector('#follow-button');
    if (followButton) {
        followButton.addEventListener('click', (event) => {
            //console.log(followButton.dataset.username)
            follow(followButton.dataset.username, csrfToken)
        });
    }

    const form = document.getElementById('compose-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
            const textarea = document.getElementById('compose-body');
            // Make sure postContent is not empty
            if (textarea.value.trim() === '') {
                alert('Post content cannot be empty.');
                return;
            }
            post(textarea);
        });
    }

    document.querySelectorAll('.edit-button').forEach(button => {
        button.addEventListener('click', (event) => {
            const postView = event.target.closest('.text-container');
            const postComment = postView.querySelector('.post-comment');
            const isEditing = postView.classList.contains('editing');
            const postContent = postView.querySelector('.post-content');
            const editContent = postView.querySelector('.edit-content');
            const textarea = postView.querySelector('.edit-textarea');
            const saveButton = postView.querySelector('.save-button');
    
            if (isEditing) {
                postContent.style.display = 'block';
                editContent.style.display = 'none';
                event.target.textContent = "Edit";
            } else {
                postContent.style.display = 'none';
                editContent.style.display = 'block';

                Object.assign(editContent.style, {
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '5px',
                    margin: '0px',
                    width: '100%',
                    alignItems: 'center'
                });
                textarea.value = postComment.textContent;
            
                // Remove any existing event listener from saveButton
                saveButton.removeEventListener('click', saveButtonClickHandler);

                // Define the save button click handler
                function saveButtonClickHandler() {
                    const newText = textarea.value;
                    postContent.style.display = 'block';
                    editContent.style.display = 'none';
                    savePost(newText, postView, event.target, csrfToken); 
                }
                // Check if the event listener is already assigned
                if (!saveButton.hasAttribute('data-listener-attached')) {
                    saveButton.addEventListener('click', saveButtonClickHandler);
                    saveButton.setAttribute('data-listener-attached', 'true'); // Set flag to indicate listener is added
                }
                event.target.textContent = "Cancel";
            }
            postView.classList.toggle('editing');
        });
    });

    document.querySelectorAll('.archive-button').forEach(button => {
        button.addEventListener('click', (event) => {
            archive(event,"post")
            
        });
    });

});

function archive(event){
    const postView = event.target.closest('.text-container');
    const postId = postView.dataset.postid;

    console.log
  
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    
    const body = {
        postId: postId,
    };
    fetch('/network/archive', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(body)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP status ${response.status}`);
        }
        return response.json();
    }) 
    .then(result => {
        event.target.textContent = result.isArchived ? "Unarchive" : "Archive"; // Toggle the button text based on the result
        console.log(result.isArchived);
        location.reload();
    })
}

function like(postId, button) {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    const url = '/network/like'; 
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken  // Include CSRF token in headers
        },
        body: JSON.stringify({ 'post_id': postId })  // Ensure you send post_id as an object
    })  
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP status ${response.status}`);
        }
        return response.json();
    })
    .then(result => {
        console.log('response: ', result);
        const likeCountElement = button.nextElementSibling;
        likeCountElement.innerHTML = result.likes > 1 ? result.likes +' Likes':result.likes +' Like' ;
    })
    .catch(error => {
        console.error('Error sending post:', error);
    });
}

function post(textarea) {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    fetch('/network/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken // Include CSRF token
        },
        body: JSON.stringify({ 'message': textarea.value }) // Send post content as JSON
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(text => { throw new Error(text); });
        }
        return response.json();
    })
    .then(result => {
        console.log('Post successful:', result);
        // Optionally clear the textarea or provide user feedback
        textarea.value = '';
        console.log('Reloading the page...');
        location.reload(); // Check if this line is reached
    })
    .catch(error => {
        console.error('Error sending post:', error);
    });
}

function follow(target_profile) {
    const url = '/network/follow';
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(target_profile)
    })  
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP status ${response.status}`);
        }
        return response.json();
    })
    .then(result => {
        console.log('response: ', result);
        //const likeCountElement = button.nextElementSibling;
        followbutton = document.querySelector('#follow-button');
        if (result.followstatus == "follow"){
            followbutton.innerHTML = "Unfollow"
        } else if (result.followstatus == "unfollow"){
            followbutton.innerHTML = "Follow"
        }

        followerscount = document.querySelector('#profile-followers');
        followSorNot = result.nbfollowers > 1 ? "Followers" : "Follower"
        followerscount.innerHTML = `${result.nbfollowers} ${followSorNot}`;
    })
    .catch(error => {
        console.error('Error sending post:', error);
    });
}

function savePost(newText, postView, editButton ) {
    // Implement the save functionality here
    console.log('New text:', newText);
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    const postId = postView.dataset.postid;

    const url = 'edit';

    const postData = {
        newText: newText,
        postId: postId
    };
  
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(postData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP status ${response.status}`);
        }
        return response.json();
    })
    .then(result => {
        // Print result of response.json();
        console.log('response: ', result);
        postView.querySelector('.post-comment').innerHTML = result.newtext;
        editButton.textContent = "Edit"
    })
    .catch(error => {
        console.error('Error sending post:', error);
    });
}

function compose_email() {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#composepost').style.display = 'none';
    const newPost = document.querySelector('#newPost');
    if (newPost) newPost.style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';

    document.querySelector("#allpostsNav").classList.remove("forumNavActive");
    document.querySelector("#followingNav").classList.remove("forumNavActive");
    document.querySelector("#inboxNav").classList.remove("forumNavActive");
    document.querySelector("#sentNav").classList.remove("forumNavActive");
    document.querySelector("#archivedNav").classList.remove("forumNavActive");
    document.querySelector("#composeNav").classList.remove("forumNavActive");
    document.querySelector("#composeNav").classList.add("forumNavActive");
}

function load_mailbox(mailbox) {
  document.querySelector('#composepost').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  const newPost = document.querySelector('#newPost');
  if (newPost) newPost.style.display = 'none';
  const emailsView = document.querySelector('#emails-view');
  emailsView.style.display = 'block';
  emailsView.innerHTML = '';
  document.querySelector("#allpostsNav").classList.remove("forumNavActive");
  document.querySelector("#followingNav").classList.remove("forumNavActive");
  document.querySelector("#inboxNav").classList.remove("forumNavActive");
  document.querySelector("#sentNav").classList.remove("forumNavActive");
  document.querySelector("#composeNav").classList.remove("forumNavActive");
  document.querySelector("#archivedNav").classList.remove("forumNavActive");

  switch(mailbox) {
    case 'inbox':
      document.querySelector("#inboxNav").classList.add("forumNavActive");
      break;
    case 'sent':
      document.querySelector("#sentNav").classList.add("forumNavActive");
      break;
    case 'archive':
      document.querySelector("#archivedNav").classList.add("forumNavActive");
      break;
    default:
      console.log('Unknown mailbox:', mailbox);
  }

  fetch(`/network/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      emails.forEach(email=>{
        console.log(email)
        
        const serverTimestamp = new Date(email.postdate);  // Assumes ISO 8601 format from server
        const userLocalTimestamp = serverTimestamp.toLocaleString();  // Converts to user's local time

        const newEmailDiv = document.createElement('div');
        newEmailDiv.className = 'text-container post ';
        newEmailDiv.setAttribute('data-postid', email.id);
        newEmailDiv.className += email.read ? 'read email' : 'unread email';
        newEmailDiv.innerHTML = `
            <div class="post-header" >
                <a href="/network/profile/${email.sender}" class="author-name">${email.sender}</a>
                <button class="archive-button" onCLick="archive(event,'email')">Archive</button>
                <i>${userLocalTimestamp}</i>
            </div>
            <div class="post-recipients">Recipients:&nbsp;<a href="/network/profile/${email.recipients}">${email.recipients}</a></div>
            <div class="post-subject">Subject: ${email.subject}</div>

            <div class="post-content" style="display: none">
                <p class="author-name"></p>
                <p class="post-body" id="email-body">${email.body}</p>
            </div>
        `;
        newEmailDiv.addEventListener('click', ()=>{
            const emailDetail = newEmailDiv.querySelector('.post-content');
            if (emailDetail.style.display === 'none' || emailDetail.style.display === '') {
                emailDetail.style.display = 'block';
            } else {
                emailDetail.style.display = 'none';
            }
            emailDetail.style.setProperty('border-top', '1px solid #196a6c', 'important');
        });
        emailsView.append(newEmailDiv);
      })
    });
}

function sendmail(){
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
  
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body-emails').value;
    console.log(body)
  
    console.log(`Sending email to URL: /emails`,"recipient",recipients);
    
    fetch('/network/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    },
      body: JSON.stringify({
          recipients: recipients,
          subject: subject,
          body: body
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log('response: ',result);
        load_mailbox('sent');
    })
}