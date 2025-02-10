# 🎵 Orthophonic

**Orthophonic** is a research-based Python library for algorithmic music composition, leveraging mathematical principles such as **zero-crossings of oscillators, non-uniform sampling, and structured event distributions**. By bridging signal processing and musical structures, Orthophonic provides a framework for generating rhythms, pitch scales, and musical sequences based on rigorous mathematical foundations.

## 🚀 Features

- **Mathematically-driven composition**: Generates musical structures using **oscillator zero-crossings** and **event spacing optimization**.
- **Harmonic & Rhythmic Generation**: Supports **equal temperament**, **custom scales**, and **rhythmic patterns**.
- **Grid-Based Event Placement**: Uses a **master grid** for time and frequency structuring.
- **Customizable Phase & Frequency Modulation**: Enables fine control over rhythm and pitch via local oscillators.
- **Seamless Integration**: Works with **Ableton Live, Max/MSP, SuperCollider**, and other DAWs.

## 📦 Installation

> Work with python 3.12

To install Orthophonic, simply run:


```bash
pip install -r requirements.txt
```

```bash
pip install -e .
```

Here’s an improved version of your **README** section with better clarity, structure, and formatting:

---

### 🎵 **Note for Ableton Users**  

You can send information directly to **Ableton Live** using **PyLive**:  
🔗 [PyLive GitHub Repository](https://github.com/ideoforms/pylive)  

To enable this functionality, you need to install **Remote Scripts** in Ableton’s folder and configure **Ableton Live** accordingly.  

📌 **Installation Guide:**  

Follow the setup instructions here:  
🔗 [AbletonOSC Installation Guide](https://github.com/ideoforms/AbletonOSC?tab=readme-ov-file#installation)  


## Run some example

```
cd examples
python drums_example.py # create a drum track in the first clip of the first track in Ableton Live
python drums_example_midi.py # export a drum track to a midi file
```
