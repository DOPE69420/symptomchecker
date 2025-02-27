
// // Import Firebase modules from the modular SDK
// import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
// import { getAuth } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
// import { getFirestore } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";

// // Firebase Configuration
// const firebaseConfig = {
//     apiKey: "AIzaSyD25aurIQY_NlBkR96HVUHFAsZRpCBfGdE",
//     authDomain: "newsletter-11ff5.firebaseapp.com",
//     projectId: "newsletter-11ff5",
//     storageBucket: "newsletter-11ff5.firebasestorage.app",
//     messagingSenderId: "442878055507",
//     appId: "1:442878055507:web:bf301eb36a7a729061e2a6"
// };

// // Initialize Firebase using modular SDK (v9+)
// const app = initializeApp(firebaseConfig);

// // Get Firestore and Auth instances
// const db = getFirestore(app);
// const auth = getAuth(app);

// // Export db and auth for use in other parts of your app
// export { auth, db };

// import { createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
// import { addDoc, collection, serverTimestamp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";
// import { auth, db } from './firebase-config.js';

// // Function to send email using SMTP
// function sendWelcomeEmail(email) {
//     Email.send({
//         Host: "smtp.gmail.com",
//         Username: "your-email@gmail.com",
//         Password: "your-gmail-app-password",
//         To: email,
//         From: "your-email@gmail.com",
//         Subject: "Welcome to Our Newsletter! 🎉",
//         Body: `Hi there! 🎉 <br><br> Thanks for subscribing to our newsletter. Stay tuned for updates! <br><br> - Your Team`
//     }).then(() => {
//         console.log("Welcome email sent successfully!");
//     }).catch((error) => {
//         console.error("Error sending email:", error);
//     });
// }

// document.getElementById('subscribeForm').addEventListener('submit', function (event) {
//     event.preventDefault();

//     const email = document.getElementById('email').value;
//     const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

//     if (email && emailRegex.test(email)) {
//         // Store email in Firestore
//         addDoc(collection(db, 'subscribers'), {
//             email: email,
//             subscribedAt: serverTimestamp()
//         })
//             .then(() => {
//                 // Create Firebase Authentication User
//                 createUserWithEmailAndPassword(auth, email, 'temporaryPassword123')
//                     .then(() => {
//                         console.log("User registered successfully!");
//                         sendWelcomeEmail(email);  // Send email
//                         alert('Thank you for subscribing! A welcome email has been sent.');
//                         document.getElementById('email').value = ''; // Clear input
//                     })
//                     .catch((error) => {
//                         console.error('Error creating user:', error.message);
//                         alert('Something went wrong. Please try again.');
//                     });
//             })
//             .catch((error) => {
//                 console.error('Error adding document:', error.message);
//                 alert('Something went wrong. Please try again.');
//             });
//     } else {
//         alert('Please enter a valid email address!');
//         document.getElementById('email').value = ''; // Clear input
//     }
// });


import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import { createUserWithEmailAndPassword, getAuth } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import { addDoc, collection, getFirestore, serverTimestamp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";

// ✅ Replace with your Firebase config
const firebaseConfig = {
    apiKey: "AIzaSyD25aurIQY_NlBkR96HVUHFAsZRpCBfGdE",
    authDomain: "newsletter-11ff5.firebaseapp.com",
    projectId: "newsletter-11ff5",
    storageBucket: "newsletter-11ff5.firebasestorage.app",
    messagingSenderId: "442878055507",
    appId: "1:442878055507:web:bf301eb36a7a729061e2a6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// Function to send email using SMTP.js
function sendWelcomeEmail(email) {
    Email.send({
        Host: "smtp.gmail.com",
        Username: "alias2001op@gmail.com",
        Password: "rajan@123",
        To: email,
        From: "alias2001op@gmail.com",
        Subject: "Welcome to Our Newsletter! 🎉",
        Body: `Hi there! 🎉 <br><br> Thanks for subscribing to our newsletter. Stay tuned for updates! <br><br> - Your Team`
    }).then(() => {
        console.log("Welcome email sent successfully!");
    }).catch((error) => {
        console.error("Error sending email:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('subscribeForm').addEventListener('submit', function (event) {
        event.preventDefault(); // ✅ Page refresh nahi hoga

        const email = document.getElementById('email').value;
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

        if (email && emailRegex.test(email)) {
            // Store email in Firestore
            addDoc(collection(db, 'subscribers'), {
                email: email,
                subscribedAt: serverTimestamp()
            })
                .then(() => {
                    // Create Firebase Authentication User
                    createUserWithEmailAndPassword(auth, email, 'temporaryPassword123')
                        .then(() => {
                            console.log("User registered successfully!");
                            sendWelcomeEmail(email);  // ✅ Email bhejega
                            alert('Thank you for subscribing! A welcome email has been sent.');
                            document.getElementById('email').value = ''; // ✅ Input clear karega
                        })
                        .catch((error) => {
                            console.error('Error creating user:', error.message);
                            alert('Something went wrong. Please try again.');
                        });
                })
                .catch((error) => {
                    console.error('Error adding document:', error.message);
                    alert('Something went wrong. Please try again.');
                });
        } else {
            alert('Please enter a valid email address!');
            document.getElementById('email').value = ''; // ✅ Input clear karega
        }
    });
});