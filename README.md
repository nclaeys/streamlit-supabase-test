# Streamlit Authentication with Supabase

This project showcases a comprehensive authentication system using Supabase as the backend, implemented with Streamlit frontends. It demonstrates how to build secure, user-friendly authentication flow.

### Streamlit App
The Streamlit application provides a user-friendly, interactive interface for user registration, login, profile management, and settings customization. It leverages Streamlit's simplicity to create a responsive web app with minimal code.

# Streamlit Supabase Authentication App

This Streamlit application demonstrates user authentication and profile management using Supabase as the backend.

## Prerequisites

- Python 3.7+
- Streamlit
- Supabase account and project

## Setup

1. Clone the repository to your local machine.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Supabase project:
   - Create a new project in Supabase
   - Enable Email Auth in Authentication > Providers

4. Create a `.env` file in the root directory with your Supabase credentials:
   ```
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_key
   ```

## Running the App

To run the Streamlit app, use the following command in your terminal:

```
streamlit run main.py
```

The app should now be running on `http://localhost:8501`.

## Features

- User Registration
- User Login
- Password Reset
- User Settings (theme, notifications, language)

## File Structure

- `main.py`: The main Streamlit app
- `utils/supabase_client.py`: Supabase client initialization
- `src/auth/`: Authentication-related functions
- `src/pages/`: Different pages of the app (home, profile, settings)

## Customization

You can customize the app by modifying the following:

- `src/pages/`: Add or modify pages
- `src/auth/`: Adjust authentication logic
- `utils/supabase_client.py`: Add more Supabase-related functions

## Troubleshooting

If you encounter any issues:

1. Ensure your Supabase credentials are correct in the `.env` file
2. Verify that you've installed all required dependencies

For more help, refer to the Streamlit and Supabase documentation.

## Security Note

This app is for demonstration purposes. In a production environment, ensure you follow best practices for security, including proper error handling and input validation.