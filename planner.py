import streamlit as st
from openai import OpenAI  # Ensure this is correctly installed or replace with the library you are using

# Initialize the OpenAI Client
client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1/",
    api_key="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"
)

# CSS to style the form, page layout, and the review section
st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #dfe9f3, #ffffff);
        padding: 20px;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }

    .container {
        max-width: 1000px;
        margin: auto;
        background-color: #ffffff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        width: 75%;
    }

    .reviews {
        width: 30%;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-left: 40px;  /* Push reviews to the right */
    }

    h1 {
        font-size: 36px;
        color: #2c3e50;
        text-align: center;
    }

    h2 {
        font-size: 24px;
        margin-bottom: 20px;
        color: #34495e;
    }

    .form-group {
        margin-bottom: 20px;
    }

    .form-group label {
        font-size: 14px;
        color: #34495e;
        margin-bottom: 8px;
        display: block;
    }

    .submit-btn {
        background-color: #3498db;
        color: white;
        font-size: 16px;
        padding: 12px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        width: 100%;
    }

    .submit-btn:hover {
        background-color: #2980b9;
    }

    footer {
        text-align: center;
        font-size: 14px;
        color: #95a5a6;
        margin-top: 30px;
    }

    .output-section {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 8px;
    }

    .review-box {
        background-color: #f1f1f1;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .review-box p {
        font-size: 14px;
        color: #2c3e50;
        font-style: italic;
    }

    .review-box h4 {
        font-size: 16px;
        color: #3498db;
        margin-top: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

# Streamlit App Setup
st.title("AI Travel Itinerary Planner 🗺✨")
st.subheader("Plan your dream trip in minutes! 🌟")

# Collect User Inputs via Streamlit
col1, col2 = st.columns([4, 2])  # Increase the width of the left column (User Input) and reduce the right column (Reviews)

with col1:
    with st.form(key='travel_form', clear_on_submit=True):
        # User's name input
        name = st.text_input("Your Name 🧑‍💻", placeholder="Enter your name", max_chars=50)

        # User's age input
        age = st.number_input("Your Age 🎂", min_value=1, max_value=150, step=1)

        # Destination input
        destination = st.text_input("Where are you traveling to? 🌍", placeholder="e.g., Paris, Japan, New York")

        # Trip duration input (1 to 28 days)
        trip_duration = st.slider("How many days? 📅", min_value=1, max_value=28, value=3)

        # Budget input
        budget = st.number_input("Enter your budget (in ₹ 💰)", min_value=1, step=1000)

        # Purpose of the trip dropdown
        purpose = st.selectbox(
            "Purpose of the Trip 🎯", 
            ["Vacation 🏖", "Business 💼", "Adventure 🌄", "Relaxation 🧘‍♂", "Cultural 🏛"]
        )

        # Preferences input (Provide reference for user)
        preferences = st.text_area(
            "Preferences 💭", 
            placeholder="Enter your trip preferences (e.g., local food 🍲, history 🏰, nature 🌳, art 🎨, hidden gems 💎)",
            height=150
        )

        # Submit button
        submit_button = st.form_submit_button("Generate Itinerary ✈")

# Display the user's input after form submission
if submit_button:
    # Validate Input
    if not name.strip() or not age or not destination.strip():
        st.error("Please provide your name 🧑‍💻, age 🎂, and destination 🌍.")
    else:
        # Prepare the conversation for AI request
        messages = [
            {
                "role": "system",
                "content": "You are a travel planner. Design detailed and personalized itineraries for users."
            },
            {
                "role": "user",
                "content": (
                    f"My name is {name} 🧑‍💻, I am {age} years old 🎂. "
                    f"Plan a {trip_duration}-day trip to {destination} 🌍 with a budget of ₹{budget} 💰. "
                    f"The purpose of the trip is {purpose} 🎯. I enjoy {preferences} 💭."
                )
            }
        ]

        # Make API Request
        with st.spinner("Generating your itinerary... 🌐"):
            try:
                # Call the chat completion API
                completion = client.chat.completions.create(
                    model="meta-llama/Llama-3.2-1B-Instruct",  # Adjust to a valid model
                    messages=messages,
                    max_tokens=500  # Adjust max tokens based on trip duration
                )
                
                # Access the content of the response
                itinerary = completion.choices[0].message.content  # Use .content to access text
                
                # Display the itinerary in a styled output section
                st.markdown('<div class="output-section">', unsafe_allow_html=True)  # Start output section
                st.success("Here’s your personalized itinerary 📜:")
                st.write(itinerary)
                st.markdown('</div>', unsafe_allow_html=True)  # End output section

            except Exception as e:
                st.error(f"An error occurred: {e} ⚠")

# Add Reviews Section on the Right (beside the input form)
with col2:
    st.markdown('### What Our Happy Travelers Say 📣')

    st.markdown("""
        <div class="review-box">
            <p>"This app made planning my vacation so much easier! It considered all my preferences and helped me pick the perfect destination. Highly recommend!"</p>
            <h4>- Sarah L., USA 🇺🇸</h4>
        </div>

        <div class="review-box">
            <p>"I was impressed by the suggestions for local food and hidden gems. The itinerary was spot on! Definitely my go-to for future travels!"</p>
            <h4>- Raj K., India 🇮🇳</h4>
        </div>

        <div class="review-box">
            <p>"A personalized experience that gave me the best of both worlds: adventure and relaxation. The itinerary had the perfect balance!"</p>
            <h4>- Emily W., Canada 🇨🇦</h4>
        </div>

        <div class="review-box">
            <p>"The trip planner understood my interests in culture and history. I had the most amazing time exploring art galleries and ancient landmarks!"</p>
            <h4>- Alex M., UK 🇬🇧</h4>
        </div>
    """, unsafe_allow_html=True)

# Add a closing line with greeting and company credit
st.markdown("""
    <footer>
        <p>Thank you for using the AI Travel Planner! 🌟</p>
        <p>Created with ❤ by [Your Company Name] 🏢 | Safe travels! ✈</p>
    </footer>
""", unsafe_allow_html=True)