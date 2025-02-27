const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");

menuBtn.addEventListener("click", (e) => {
  navLinks.classList.toggle("open");

  const isOpen = navLinks.classList.contains("open");
  menuBtnIcon.setAttribute(
    "class",
    isOpen ? "ri-close-line" : "ri-menu-3-line"
  );
});

navLinks.addEventListener("click", (e) => {
  navLinks.classList.remove("open");
  menuBtnIcon.setAttribute("class", "ri-menu-3-line");
});

const scrollRevealOption = {
  distance: "50px",
  origin: "bottom",
  duration: 1000,
};

ScrollReveal().reveal(".header__image img", {
  ...scrollRevealOption,
  origin: "right",
  interval: 500,
});
ScrollReveal().reveal(".header__content h1", {
  ...scrollRevealOption,
  delay: 1500,
});
ScrollReveal().reveal(".header__content .section__description", {
  ...scrollRevealOption,
  delay: 2000,
});
ScrollReveal().reveal(".header__content form", {
  ...scrollRevealOption,
  delay: 2500,
});

ScrollReveal().reveal(".choose__image img", {
  ...scrollRevealOption,
  origin: "left",
});
ScrollReveal().reveal(".choose__content .section__subheader", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".choose__content .section__header", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".choose__list li", {
  ...scrollRevealOption,
  delay: 1500,
  interval: 500,
});

const swiper = new Swiper(".swiper", {
  slidesPerView: 3,
  spaceBetween: 0,
  loop: true,
});

ScrollReveal().reveal(".explore__image img", {
  ...scrollRevealOption,
  origin: "right",
});
ScrollReveal().reveal(".explore__content .section__subheader", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".explore__content .section__header", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".explore__content .section__description", {
  ...scrollRevealOption,
  delay: 1500,
});
ScrollReveal().reveal(".explore__content .explore__btn", {
  ...scrollRevealOption,
  delay: 2000,
});
ScrollReveal().reveal(".explore__grid div", {
  duration: 1000,
  delay: 2500,
  interval: 500,
});

const next = document.getElementById("next");
const prev = document.getElementById("prev");
const clientCards = Array.from(document.querySelectorAll(".client__card"));

next.addEventListener("click", (e) => {
  for (let index = 0; index < clientCards.length; index++) {
    if (clientCards[index].classList.contains("active")) {
      const nextIndex = (index + 1) % clientCards.length;
      clientCards[index].classList.remove("active");
      clientCards[nextIndex].classList.add("active");
      break;
    }
  }
});

prev.addEventListener("click", (e) => {
  for (let index = 0; index < clientCards.length; index++) {
    if (clientCards[index].classList.contains("active")) {
      const prevIndex = (index ? index : clientCards.length) - 1;
      clientCards[index].classList.remove("active");
      clientCards[prevIndex].classList.add("active");
      break;
    }
  }
});

ScrollReveal().reveal(".subscribe__container .section__header", {
  ...scrollRevealOption,
});
ScrollReveal().reveal(".subscribe__container .section__description", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".subscribe__container form", {
  ...scrollRevealOption,
  delay: 1000,
});



// Add an event listener to the button to handle the redirection on click
document.getElementById('login-btn').addEventListener('click', function () {
  // Redirect the user to another page (page2.html in this case)
  window.location.href = './auth/auth.html';  // Replace with your target URL
});



// document.getElementById('search-form').addEventListener('submit', function (e) {
//   e.preventDefault(); // Prevent form submission

//   const age = document.getElementById('age').value;
//   const gender = document.getElementById('gender').value;
//   const location = document.getElementById('location').value;

//   // Validate that age is a positive integer
//   if (age && parseInt(age) <= 0) {
//     alert('Please enter a valid age.');
//     return;
//   }

//   // If gender or location is not selected, show an error message
//   if (!gender || !location) {
//     alert('Please fill in all the required fields.');
//     return;
//   }

//   // Show additional details section
//   document.getElementById('additional-details').style.display = 'block';
// });


// document.getElementById('subscribeForm').addEventListener('submit', function (event) {
//   event.preventDefault();

//   const email = document.getElementById('email').value;

//   if (email) {
//     alert(`Thank you for subscribing, ${email}! We'll keep you updated.`);
//     // Here, you could send the email to your server or a subscription service
//   } else {
//     alert('Please enter a valid email address!');
//   }
// });


// document.getElementById('subscribeForm').addEventListener('submit', function (event) {
//   // Prevent the default form submission behavior
//   event.preventDefault();

//   // Get the email entered by the user
//   const email = document.getElementById('email').value;

//   // Check if the email field is not empty
//   if (email) {
//     // You can send the email to the backend here, or show an alert as a placeholder
//     alert(`Thank you for subscribing, We'll keep you updated.`);

//     // Optional: Clear the input field after submission
//     document.getElementById('email').reset(); // Clear input after submission

//   } else {
//     // If email is not valid, show a message
//     alert('Please enter a valid email address!'); s
//   }
// });


// document.getElementById('subscribeForm').addEventListener('submit', function (event) {
//   // Prevent the default form submission behavior
//   event.preventDefault();

//   // Get the email entered by the user
//   const email = document.getElementById('email').value;

//   // Regular expression for validating email format
//   const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

//   // Check if the email is not empty and matches the email format
//   if (email && emailRegex.test(email)) {
//     // You can send the email to the backend here, or show an alert as a placeholder
//     alert(`Thank you for subscribing, We'll keep you updated.`);

//     // Clear the input field after submission
//     document.getElementById('email').value = '';

//   } else {
//     // If email is invalid, show a message
//     alert('Please enter a valid email address!');

//     // Clear the input field after invalid submission
//     document.getElementById('email').value = '';
//   }
// });


// app.js

// import { createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
// import { addDoc, collection, serverTimestamp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";
// import { auth, db } from './firebase-config.js';

// document.getElementById('subscribeForm').addEventListener('submit', function (event) {
//   event.preventDefault(); // Prevent the form from submitting

//   const email = document.getElementById('email').value;

//   // Regular expression for validating email format
//   const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

//   if (email && emailRegex.test(email)) {
//     // Store the email in Firestore
//     addDoc(collection(db, 'subscribers'), {
//       email: email,
//       subscribedAt: serverTimestamp()
//     })
//       .then(() => {
//         // Create a user in Firebase Authentication (this will trigger Firebase to send a welcome email)
//         createUserWithEmailAndPassword(auth, email, 'temporaryPassword123')
//           .then(() => {
//             alert('Thank you for subscribing! We will keep you updated.');
//             document.getElementById('email').value = ''; // Clear the input
//           })
//           .catch((error) => {
//             console.error('Error creating user:', error.message);
//             alert('Something went wrong. Please try again.');
//           });
//       })
//       .catch((error) => {
//         console.error('Error adding document:', error.message);
//         alert('Something went wrong. Please try again.');
//       });
//   } else {
//     alert('Please enter a valid email address!');
//     document.getElementById('email').value = ''; // Clear the input
//   }
// });
document.getElementById("predict-button").addEventListener("click", function () {
  let symptoms = document.getElementById("symptom-input").value;

  fetch("http://127.0.0.1:8000/DrAi/get_diseases/", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({ symptoms: symptoms })
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById("result").innerText = "Predicted Disease: " + data.disease;
  })
  .catch(error => console.error("Error:", error));
});



