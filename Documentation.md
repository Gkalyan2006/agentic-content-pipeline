# Agentic AI Content Pipeline – Project Documentation

## 1. Introduction

This project implements an Agentic AI system that automates content creation from research to publication.

Instead of using a single AI call, the system is divided into specialized agents. Each agent performs a focused task and passes results to the next agent.

The pipeline produces:

- Blog articles
- Social media posts
- Email newsletters
- SEO optimized content
- Automatically published WordPress posts

---

## 2. Objectives

- Automate content generation
- Reduce manual editing effort
- Maintain brand voice
- Optimize SEO
- Enable draft compression using ScaleDown
- Publish content automatically
- Demonstrate agent-based architecture

---

## 3. System Architecture

Pipeline Flow:

Topic Agent  
↓  
Research Agent  
↓  
Writer Agent (Blog + Social + Email)  
↓  
Editor Agent (Brand Voice)  
↓  
SEO Agent (Optimization + A/B Headlines)  
↓  
ScaleDown Agent  
↓  
WordPress Publish Agent  

Each agent is implemented as an independent Python module.

---

## 4. Agents Description

### 4.1 Topic Agent
Generates content topics based on input keyword.

### 4.2 Research Agent
Collects summarized information using LLM API.

### 4.3 Writer Agent
Creates:

- Blog article
- Instagram caption
- LinkedIn post
- Email newsletter

Uses research data as input.

### 4.4 Editor Agent
Applies:

- Grammar correction
- Brand voice consistency
- Content clarity

### 4.5 SEO Agent
Optimizes content for:

- Search engine ranking
- Keyword placement
- Headings
- Meta description

Also generates two headline variations for A/B testing.

### 4.6 ScaleDown Agent
Compresses multiple draft versions into a single optimized output while maintaining context.

Reduces revision history size by approximately 80%.

### 4.7 Publish Agent
Uses WordPress REST API to automatically publish content.

---

## 5. Technology Stack

- Python
- Groq LLM API
- Requests library
- WordPress REST API

---

## 6. Folder Structure

