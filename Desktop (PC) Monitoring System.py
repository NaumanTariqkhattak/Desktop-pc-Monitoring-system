#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Install the required library
# pip install wmi

import wmi
import time

def get_hardware_components():
    w = wmi.WMI()
    components = []

    for item in w.Win32_PnPEntity():
        if item.Caption is not None:
            components.append(item.Caption)

    return components

previous_components = set(get_hardware_components())

while True:
    current_components = set(get_hardware_components())

    # Check for hardware additions
    added_components = current_components - previous_components
    if added_components:
        print("Hardware addition(s):")
        for component in added_components:
            print(component)

    # Check for hardware removals
    removed_components = previous_components - current_components
    if removed_components:
        print("Hardware removal(s):")
        for component in removed_components:
            print(component)

    # Update previous components for the next iteration
    previous_components = current_components

    time.sleep(2)  # Check every 2 seconds


# In[ ]:




