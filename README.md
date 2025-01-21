
# Dynamical System - Data Generator

**Data-based modelling** often requires an input-output dataset where a *Dynamical System* is excited with an input sequence, say $u\left[k\right],\ k=1, 2, 3, ... $. And the response of the system $y\left[k\right]$, corresponding to each $u\left[k\right]$, is measured.

This code generates a Skyline signal (aka, **A**mplitude-modulated **P**seudo **R**andom **B**inary **S**equence or APRBS) to excite nonlinear systems. Currently, the code supports

* Robotic Arm System
* Magnetic Levitation System
* Van Der Pol Oscillator

The following image shows the APRBS signal (red) used to excite a Van Der Pol oscillator and its response (blue).

<img alt='Excited-VanDerPol-Oscillator' src='../test-2025-01-11/assets/VanDerPol-Dataset.png'>