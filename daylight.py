import numpy as np

def hour_to_daylight(hour):
    '''
    # Calculate daylight value using cosine
    
    Example: 
    hours = [0, 6, 12, 18, 23]  # Midnight, 6am, Noon, 6pm, 11pm
    daylight_values = [hour_to_daylight(hour) for hour in hours]
    for hour, daylight in zip(hours, daylight_values):
        print(f"Hour: {hour}, Daylight Value: {daylight:.4f}")
    '''
  
    daylight = np.cos((2 * np.pi * hour) / 24)) * (-1)
    return daylight
