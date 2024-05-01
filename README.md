# peregrinEYE
![My Example Image](peregrin_eye_logo.jpg)
AI-powered audio guidance for the visually impaired. Explore your surroundings, identify objects, and navigate with confidence.

## Inspiration

As a programmer, I spend countless hours staring at code.  One day,  eye strain forced me to confront the world with blurry vision. This experience highlighted the profound impact of sight on our daily lives. It sparked a question: could AI, the very technology that caused this temporary setback,  become a tool to assist when my vision needed a break?

## What it does
peregrinEYE is a pocket-sized AI assistant designed to empower the visually impaired. 

Here's what it can do right now:

* Image Description: Take a picture anywhere with sufficient light, and peregrinEYE will instantly describe the elements in the image from your perspective, providing rich details. It saves both the picture and the audio description as an MP3 for later reference.
* Coming in days: Interactive Guidance: Within days, peregrinEYE will take things a step further. Simply tell it what you're looking for in the captured image, and it will provide audio instructions to help you reach the object, navigate around obstacles, or interact with your surroundings.

## How we built it
peregrinEYE leverages some powerful tools:

* Image Description Engine: We utilize the robust Gemini vision model to analyze pictures taken by the device and generate detailed descriptions.
* Text-to-Speech (TTS): Google's Text-to-Speech (gTTS) engine converts the descriptive text into clear audio for users.
* Hardware: The core components include a Raspberry Pi Zero 2W, an Adafruit Voice Bonnet for audio input and output, and a UPS Lite for reliable power supply. Python serves as the primary programming language.
* Efficient Storage: Photos are saved in JPEG format for space optimization, while conversations are stored as MP3 files.

## Challenges we ran into
* Miniaturization: Cramming all the necessary code and hardware for on-device AI processing into a small, handheld device proved challenging. Finding the right components and casings was a key hurdle.
* Multitasking Management: A significant ongoing challenge lies in managing multiple services simultaneously. This includes voice generation, AI API calls, button and microphone inputs, and ensuring a fast response time from the AI.

## Accomplishments that we're proud of
peregrinEYE is still under development, but we've achieved some significant milestones:

*Functional Prototype: A working model that demonstrates core functionalities like object identification and basic color description.
Enthusiastic User Feedback: Early testers have expressed excitement about the potential of peregrinEYE to improve their daily lives.*

## What we learned
This project has been a valuable learning experience:

* The Power of Vision Models: We gained a deeper understanding of how vision models work and how they can link different images to provide insightful information about the world around us.
Multitasking Mastery: The importance of efficiently managing multiple processes running concurrently on a limited-resource device became abundantly clear.
* Minimalist Design for Accessibility: We prioritized creating a user-friendly and minimalistic device that can be easily used by anyone, especially those with visual impairments.

## What's next for peregrinEYE
* PrevisAI: We envision a system within peregrinEYE called "PrevisAI" that can anticipate your needs and movements based on the images you provide, offering proactive assistance.
* Beyond the Initial Prototype: We're actively working on integrating the features you mentioned, including color identification, object location assistance, and even walkthrough assistance for video games.
* Real-Time Obstacle Detection: peregrinEYE will evolve to not only identify objects but also detect potential obstacles in real-time, enhancing safe navigation for users.
