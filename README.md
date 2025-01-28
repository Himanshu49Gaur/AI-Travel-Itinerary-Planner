# AI-Travel-Itinerary-Planner

Project Report: AI Travel Itinerary Planner
 Introduction
The AI Travel Itinerary Planner is a user-friendly application designed to help users create personalized travel itineraries based on their input, such as destination, budget, trip duration, purpose, and preferences. The interface is visually appealing, interactive, and easy to use, making the trip-planning process seamless.

Features
User Inputs
•	Name and Age: Basic details about the user.
•	Destination: The place where the user intends to travel.
•	Budget: User can enter their trip budget in rupees.
•	Trip Duration: Selectable duration of up to 28 days.
•	Purpose: A dropdown menu with options like Vacation, Adventure, Business, and more.
•	Preferences: A text box with examples (e.g., local food, history) for better guidance.
Additional Elements
•	Review Section: A right-aligned section featuring reviews from past users with names and feedback to build trust and credibility.
•	Image Section: A left-aligned section showcasing travel-related images to enhance the visual appeal.
•	Responsive Layout: Optimized user input section with increased width to ensure a clean and organized layout.



Code Implementation
The project combines Streamlit for the web app and custom HTML/CSS for a highly styled user interface.
Code Highlights
1.	Streamlit for Functionality:
o	Captures user input via text boxes, dropdown menus, sliders, and text areas.
o	Displays results dynamically after API interaction.
o	Uses layout features (st.columns, st.markdown) for a polished design.
2.	HTML/CSS for Styling:
o	Custom styles ensure the UI looks professional and visually appealing.
o	A review section and an image gallery fill the page while maintaining alignment.
3.	Prompts and Integration:
o	Prompts guide users for preferences, such as travel interests.
o	The project includes structured logic to validate user inputs and interact with the API.
 API Overview
API Used: Hugging Face Inference API
The project uses the Hugging Face Inference API to generate travel itineraries. This API enables interaction with language models, providing detailed and coherent itinerary suggestions tailored to the user's input.

•	Base URL: https://api-inference.huggingface.co/v1/

•	Model: meta-llama/Llama-3.2-1B-Instruct

•	Key Features:
o	Natural Language Processing: The model processes user queries to generate detailed itineraries.
o	Customization: Responds to user-specific preferences, destination, and budget.
Integration with Streamlit:
•	The user input is converted into a structured message format and sent to the API.
•	The API responds with a text-based itinerary, which is displayed to the user in real time.


Example API call:

completion = client.chat.completions.create(

    model="meta-llama/Llama-3.2-1B-Instruct",
    messages=messages,
    max_tokens=500
)

. Reasoning and Thought Process
Design and User Experience
•	The layout is carefully structured to ensure user inputs are central, as they are the core functionality.
•	Reviews and images are added to create a balanced and engaging interface.
API Choice
•	Hugging Face's models were chosen for their high-quality natural language understanding and response generation.
•	The API offers flexibility in designing responses tailored to specific user inputs.


Results
•	The app dynamically generates personalized travel itineraries based on user-provided information.
•	The polished UI and added elements like reviews and images improve user engagement.
•	The inclusion of AI-generated responses ensures the application provides value to users.

Conclusion
The AI Travel Itinerary Planner is a practical and user-friendly tool that combines advanced AI capabilities with an attractive, responsive interface. It demonstrates the power of integrating APIs like Hugging Face with Streamlit to create meaningful and interactive applications.
