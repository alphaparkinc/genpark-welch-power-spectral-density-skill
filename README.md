# genpark-welch-power-spectral-density-skill

[![CI](https://github.com/alphaparkinc/genpark-welch-power-spectral-density-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-welch-power-spectral-density-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> Welch's periodogram method for Power Spectral Density (PSD) estimation using Hann-windowed overlapping signal segmentation.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / DSP Pipeline] -->|Input Signal| Engine[genpark-welch-power-spectral-density-skill]
    Engine --> Transform[Frequency / Wavelet Decomposition]
    Transform --> Spectrum[(Spectral Representation)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Mathematically rigorous implementations of Fourier, Wavelet, Cosine, and Hilbert transforms.
- Native Model Context Protocol (MCP) server support for AI agent signal analysis.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-welch-power-spectral-density-skill.git
cd genpark-welch-power-spectral-density-skill
```

## Quickstart

```bash
python example_usage.py
```
