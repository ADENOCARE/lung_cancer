# How to Obtain a Google Generative AI API Key

Follow these steps to get an API key for the Google Generative AI (Gemini API):

1. **Create a Google Cloud Account**
   - Visit [Google Cloud Console](https://console.cloud.google.com/).
   - Sign in with your Google account or create a new one.

2. **Create a New Project**
   - In the Google Cloud Console, click on the project dropdown in the top navigation bar.
   - Click **"New Project"** and provide a name for your project (e.g., "Lung Cancer Analysis").
   - Click **"Create"**.

3. **Enable the Generative AI API**
   - Go to the **API & Services** section in the left-hand menu.
   - Click **"Enable APIs and Services"**.
   - Search for **"Generative AI API"** (or "Gemini API") in the API library.
   - Click on it and then click **"Enable"**.

4. **Set Up API Credentials**
   - Navigate to **API & Services > Credentials**.
   - Click **"Create Credentials"** and select **"API Key"**.
   - A new API key will be generated. Copy this key.

5. **Restrict the API Key (Optional but Recommended)**
   - Click on the **Edit** icon next to your API key.
   - Under **Key Restrictions**, you can:
     - Restrict the key to specific IP addresses or domains.
     - Restrict the key to specific APIs (e.g., Generative AI API).
   - Save the changes.

6. **Add the API Key to Your Project**
   - Open the `.env` file in your project directory.
   - Add the following line:
     ```env
     GOOGLE_GENAI_API_KEY=your_api_key_here
     ```
   - Replace `your_api_key_here` with the API key you copied.

7. **Test the API Key**
   - Run your application and ensure the API key is working correctly.
   - If you encounter issues, double-check the key restrictions and ensure the Generative AI API is enabled.

---

### Example [.env](http://_vscodecontentref_/3) File
```env
GOOGLE_GENAI_API_KEY=your_api_key_here

---

8. **Apply Migrations**

    Run the following command to apply database migrations:

    ```bash
    python manage.py migrate
    ```

9. **Run the Development Server**

    Start the Django development server by running:

    ```bash
    python manage.py runserver
    ```

    - The server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).