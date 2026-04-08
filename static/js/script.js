document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('contact-form').addEventListener('submit', function(e) {
        let isValid = true;
        
        // Clear previous errors
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
        document.querySelectorAll('.error, .success').forEach(el => {
            el.classList.remove('error', 'success');
        });
        
        // Get form fields
        const name = document.getElementById('id_name');
        const email = document.getElementById('id_email');
        const subject = document.getElementById('id_subject');
        const message = document.getElementById('id_message');
        
        // Validate Name
        if (name.value.trim().length < 3) {
            document.getElementById('name-error').textContent = 'Name must be at least 3 characters';
            name.classList.add('error');
            isValid = false;
        } else {
            name.classList.add('success');
        }
        
        // Validate Email
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email.value.trim())) {
            document.getElementById('email-error').textContent = 'Please enter a valid email address';
            email.classList.add('error');
            isValid = false;
        } else {
            email.classList.add('success');
        }
        
        // Validate Subject
        if (subject.value.trim().length < 3) {
            document.getElementById('subject-error').textContent = 'Subject must be at least 3 characters';
            subject.classList.add('error');
            isValid = false;
        } else {
            subject.classList.add('success');
        }
        
        // Validate Message
        if (message.value.trim().length < 10) {
            document.getElementById('message-error').textContent = 'Message must be at least 10 characters';
            message.classList.add('error');
            isValid = false;
        } else {
            message.classList.add('success');
        }
        
        // Prevent submission if invalid
        if (!isValid) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    });

    // Real-time validation
    document.querySelectorAll('#contact-form input, #contact-form textarea').forEach(field => {
        field.addEventListener('blur', function() {
            // Trigger validation on blur
            const errorSpan = document.getElementById(this.id.replace('id_', '') + '-error');
            
            if (this.value.trim().length === 0) {
                errorSpan.textContent = 'This field is required';
                this.classList.add('error');
                this.classList.remove('success');
            } else {
                errorSpan.textContent = '';
                this.classList.remove('error');
                this.classList.add('success');
            }
        });
    });
});

// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById('contact-form').addEventListener('submit', function(e) {
//         let isValid = true;
        
//         // Clear previous errors
//         document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
//         document.querySelectorAll('.error, .success').forEach(el => {
//             el.classList.remove('error', 'success');
//         });
        
//         // Get form fields
//         const name = document.getElementById('id_name');
//         const email = document.getElementById('id_email');
//         const subject = document.getElementById('id_subject');
//         const message = document.getElementById('id_message');
        
//         // Validate Name
//         if (name.value.trim().length < 3) {
//             document.getElementById('name-error').textContent = 'Name must be at least 3 characters';
//             name.classList.add('error');
//             isValid = false;
//         } else {
//             name.classList.add('success');
//         }
        
//         // Validate Email
//         const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//         if (!emailPattern.test(email.value.trim())) {
//             document.getElementById('email-error').textContent = 'Please enter a valid email address';
//             email.classList.add('error');
//             isValid = false;
//         } else {
//             email.classList.add('success');
//         }
        
//         // Validate Subject
//         if (subject.value.trim().length < 3) {
//             document.getElementById('subject-error').textContent = 'Subject must be at least 3 characters';
//             subject.classList.add('error');
//             isValid = false;
//         } else {
//             subject.classList.add('success');
//         }
        
//         // Validate Message
//         if (message.value.trim().length < 10) {
//             document.getElementById('message-error').textContent = 'Message must be at least 10 characters';
//             message.classList.add('error');
//             isValid = false;
//         } else {
//             message.classList.add('success');
//         }
        
//         // Prevent submission if invalid
//         if (!isValid) {
//             e.preventDefault();
//             window.scrollTo({ top: 0, behavior: 'smooth' });
//         }
//     });

//     // Real-time validation
//     document.querySelectorAll('#contact-form input, #contact-form textarea').forEach(field => {
//         field.addEventListener('blur', function() {
//             // Trigger validation on blur
//             const errorSpan = document.getElementById(this.id.replace('id_', '') + '-error');
            
//             if (this.value.trim().length === 0) {
//                 errorSpan.textContent = 'This field is required';
//                 this.classList.add('error');
//                 this.classList.remove('success');
//             } else {
//                 errorSpan.textContent = '';
//                 this.classList.remove('error');
//                 this.classList.add('success');
//             }
//         });
//     });
// });