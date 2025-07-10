# Accent Virtual Agent

A sophisticated AI-powered voice agent for debt collection calls, built with real-time speech recognition, natural language processing, and text-to-speech capabilities. This application provides a professional and compliant voice interface for engaging with debtors, verifying identities, and discussing repayment options.

## 🎯 Overview

The Accent Virtual Agent is designed to handle outbound debt collection calls with a focus on compliance, professionalism, and effective communication. The agent, named "Ali," represents Aiqon (a debt collection company) and follows structured call flows while handling various objections and scenarios that may arise during debt collection conversations.

## ✨ Features

### Core Capabilities
- **Real-time Voice Communication**: WebRTC-based audio streaming for seamless voice interactions
- **Speech-to-Text**: Deepgram-powered real-time transcription with smart formatting
- **Natural Language Processing**: Azure OpenAI GPT-4 integration for intelligent conversation handling
- **Text-to-Speech**: ElevenLabs voice synthesis with natural-sounding speech
- **Voice Activity Detection**: Silero VAD for efficient audio processing
- **Email Integration**: Automated email sending functionality for follow-up communications

### Professional Features
- **Compliant Call Flow**: Structured conversation flow following debt collection regulations
- **Identity Verification**: Secure verification processes following PDPA guidelines
- **Objection Handling**: Comprehensive scripts for handling common debtor objections
- **Payment Plan Discussion**: Automated assistance with repayment option discussions
- **Call Recording Compliance**: Built-in compliance features for call recording notifications

## 🏗️ Architecture

The application is built using a modern microservices architecture with the following components:

- **FastAPI Backend**: RESTful API server handling WebRTC connections and pipeline management
- **WebRTC Transport**: Real-time audio streaming between client and server
- **Pipeline Processing**: Multi-stage audio processing pipeline (STT → LLM → TTS)
- **Azure Services**: OpenAI GPT-4 for conversation intelligence
- **Deepgram**: High-accuracy speech recognition
- **ElevenLabs**: Natural-sounding text-to-speech synthesis

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher
- Valid API keys for the following services:
  - Azure OpenAI (GPT-4)
  - Deepgram (Speech-to-Text)
  - ElevenLabs (Text-to-Speech)
  - Azure Communication Services (Email)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Accent Virtual Agent"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:
   ```env
   # Azure OpenAI Configuration
   AZURE_OPENAI_API_KEY=your_azure_openai_api_key
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint

   # Deepgram Configuration
   DEEPGRAM_API_KEY=your_deepgram_api_key

   # ElevenLabs Configuration
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ELEVENLABS_VOICE_ID=your_elevenlabs_voice_id
   
   > **📝 ElevenLabs Setup Guide**
   > 
   > ElevenLabs provides high-quality text-to-speech synthesis. Follow these detailed steps to set up your ElevenLabs account and obtain the required credentials:
   > 
   > ### Step 1: Create ElevenLabs Account
   > 1. Visit [ElevenLabs.io](https://elevenlabs.io)
   > 2. Click "Sign Up" and create a free account
   > 3. Verify your email address
   > 4. Complete your profile setup
   > 
   > ### Step 2: Get Your API Key
   > 1. Log in to your ElevenLabs dashboard
   > 2. Navigate to your profile settings (usually in the top-right corner)
   > 3. Look for the "API Key" section
   > 4. Click "Copy" to copy your API key
   > 5. **Important**: Keep this key secure and never share it publicly
   > 
   > ![ElevenLabs API Key Setup] ![alt text](<imgs/api (eleven labs).png>)
   > 
   > ### Step 3: Choose Your Voice
   > 1. Go to the "Voice Library" section in your dashboard
   > 2. Browse through available voices (free tier includes several options)
   > 3. Listen to voice samples to find one that matches your needs
   > 4. Consider factors like:
   >    - **Language**: Ensure the voice supports your target language
   >    - **Tone**: Professional, friendly, or authoritative
   >    - **Gender**: Male or female voice preference
   >    - **Accent**: Regional accent preferences
   > 
   > ### Step 4: Get Your Voice ID
   > 1. Select your preferred voice from the Voice Library
   > 2. Click on the voice to open its details
   > 3. Look for the "Voice ID" field (usually a long string of characters)
   > 4. Copy the Voice ID
   > 5. The Voice ID I am using is "NpVSXJvYSdIbjOaMbShj"
   > 
   > ![ElevenLabs Voice ID Setup] ![alt text](<imgs/voice id (eleven labs).png>)
   > 
   > ### Step 5: Test Your Setup
   > 1. Add your API key and Voice ID to the `.env` file
   > 2. Run the application
   > 3. Test the voice synthesis to ensure it's working correctly
   > 
   > ### Voice Configuration Tips
   > - **Free Tier Limits**: Free accounts have monthly character limits
   > - **Voice Cloning**: You can clone your own voice (requires paid plan)
   > - **Custom Voices**: Create custom voices for specific use cases
   > - **Voice Settings**: Adjust stability, similarity, and style in the code
   > 
   > ### Troubleshooting ElevenLabs
   > - **API Key Invalid**: Ensure you've copied the full key without extra spaces
   > - **Voice ID Not Found**: Verify the Voice ID exists in your account
   > - **Rate Limits**: Free tier has usage limits; consider upgrading for production use
   > - **Audio Quality**: Adjust stability and similarity settings for better quality

   # Azure Communication Services (Email)
   ACS_CONNECTION_STRING=your_acs_connection_string
   SENDER_ADDRESS=your_sender_email@domain.com
   RECIPIENT_ADDRESS=your_recipient_email@domain.com
   ```

## 🎮 Usage

### Starting the Application

1. **Run the main application**
   ```bash
   python main_v2.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8000`
   - The application will redirect you to the WebRTC client interface

### Web Interface

The application provides a web-based interface where you can:
- Initiate voice calls with the AI agent
- View real-time transcription of conversations
- Monitor call status and connection quality
- Access call history and logs

### API Endpoints

- `GET /`: Redirects to the web client interface
- `POST /api/offer`: Handles WebRTC connection offers and establishes peer connections

## 🔧 Configuration

### Voice Settings

The TTS (Text-to-Speech) settings can be configured in `main_v2.py`:

```python
tts = ElevenLabsTTSService(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
    voice_id=os.getenv("ELEVENLABS_VOICE_ID"),
    params=ElevenLabsTTSService.InputParams(
        language=ElevenLabsLanguage.EN,
        stability=0.7,        # Voice stability (0-1)
        similarity_boost=0.8, # Voice similarity (0-1)
        style=0.5,           # Voice style (0-1)
        use_speaker_boost=True,
        speed=0.8            # Speech speed (0-1)
    )
)
```

### Speech Recognition Settings

Deepgram STT settings can be modified in `main_v2.py`:

```python
stt = DeepgramSTTService(
    api_key=os.getenv("DEEPGRAM_API_KEY"),
    live_options=LiveOptions(
        model="nova-2-general",  # Speech recognition model
        language="en-US",        # Language setting
        smart_format=True,       # Enable smart formatting
        vad_events=True          # Enable voice activity detection
    )
)
```

## 📞 Call Flow

The application follows a structured call flow:

1. **Greeting & Identification**: Agent introduces themselves and requests to speak with the debtor
2. **Verification Process**: Confirms identity using IC number or date of birth
3. **Discussion**: Explains the purpose of the call and discusses payment options
4. **Payment Plan Selection**: Offers various repayment plans
5. **Closing**: Handles follow-up arrangements and call conclusion

### Objection Handling

The system includes comprehensive scripts for handling common objections:
- Wrong number claims
- Identity verification refusals
- Fraud accusations
- Settlement claims
- Account ownership denials
- Harassment complaints
- Financial hardship claims

## 🔒 Compliance & Security

- **PDPA Compliance**: Follows Personal Data Protection Act guidelines
- **Identity Verification**: Secure verification processes
- **Call Recording**: Proper notification and consent handling
- **Data Protection**: Secure handling of sensitive information

## 🛠️ Development

### Project Structure

```
Accent Virtual Agent/
├── main_v2.py          # Main application entry point
├── email_tool.py       # Email sending functionality
├── utils.py           # System message and utilities
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

### Key Components

- **`main_v2.py`**: FastAPI application with WebRTC handling and pipeline setup
- **`email_tool.py`**: Azure Communication Services integration for email functionality
- **`utils.py`**: Contains the system message defining the agent's personality and call flow

## 🐛 Troubleshooting

### Common Issues

1. **WebRTC Connection Issues**
   - Ensure your browser supports WebRTC
   - Check firewall settings for WebRTC traffic
   - Verify STUN server connectivity

2. **Audio Quality Issues**
   - Check microphone permissions in the browser
   - Ensure stable internet connection
   - Verify audio device settings

3. **API Key Errors**
   - Verify all environment variables are set correctly
   - Check API key validity and quotas
   - Ensure proper service endpoints

### Logs

The application uses Loguru for logging. Check the console output for detailed logs and error messages.

## 📄 License

[Add your license information here]

## 🤝 Contributing

[Add contribution guidelines here]

## 📞 Support

For support and questions, please contact [your contact information].

---

**Note**: This application is designed for professional debt collection use. Ensure compliance with all applicable laws and regulations in your jurisdiction before deployment. 