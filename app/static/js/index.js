import { submitContactForm } from "./form_submission.js";

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form');
    form.addEventListener('submit', submitContactForm);
});
