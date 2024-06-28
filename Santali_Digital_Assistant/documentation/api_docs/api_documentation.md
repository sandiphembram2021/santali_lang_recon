# Santali Digital Assistant API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [Endpoints](#endpoints)
   - [User Management](#user-management)
   - [Speech Recognition](#speech-recognition)
   - [Natural Language Processing (NLP)](#natural-language-processing-nlp)
   - [Knowledge Base](#knowledge-base)
   - [Voice Synthesis](#voice-synthesis)
   - [Feedback](#feedback)
4. [Error Handling](#error-handling)
5. [Rate Limiting](#rate-limiting)
6. [API Examples](#api-examples)

## Introduction
This document provides an overview of the API endpoints for the Santali Digital Assistant. The API allows interaction with the assistant through various modules such as user management, speech recognition, NLP, knowledge base, voice synthesis, and feedback.

## Authentication
### Endpoint: `POST /api/login`
Authenticates a user and returns a JWT token.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "userpassword"
}

{
  "token": "your.jwt.token.here"
}

{
  "name": "User Name",
  "email": "user@example.com",
  "password": "userpassword"
}

{
  "message": "User registered successfully"
}

{
  "id": "user_id",
  "name": "User Name",
  "email": "user@example.com"
}

{
  "text": "converted text from speech"
}
{
  "text": "User input text in Santali"
}
{
  "intent": "user_intent",
  "entities": {
    "entity1": "value1",
    "entity2": "value2"
  }
}
{
  "entries": [
    {
      "id": "entry_id",
      "title": "Entry Title",
      "content": "Entry Content"
    },
    {
      "id": "entry_id",
      "title": "Entry Title",
      "content": "Entry Content"
    }
  ]
}
{
  "title": "New Entry Title",
  "content": "New Entry Content"
}
{
  "message": "Entry added successfully"
}
{
  "title": "Updated Entry Title",
  "content": "Updated Entry Content"
}
{
  "message": "Entry updated successfully"
}
{
  "message": "Entry deleted successfully"
}
{
  "text": "Text to be converted to speech"
}
{
  "audio_url": "url_to_generated_audio_file"
}
{
  "feedback": "User feedback text"
}
{
  "message": "Feedback submitted successfully"
}
{
  "feedback": [
    {
      "id": "feedback_id",
      "user": "user_id",
      "feedback": "User feedback text"
    },
    {
      "id": "feedback_id",
      "user": "user_id",
      "feedback": "User feedback text"
    }
  ]
}

