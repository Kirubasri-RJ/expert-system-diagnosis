# expert-system-diagnosis
A rule based expert system that diagnoses a specific problem based on user reported symptoms. 
How It Works

The system asks the user a series of yes/no questions about symptoms their car is showing (e.g. "Does the car fail to start?", "Is the engine overheating?"). It then matches the reported symptoms against a set of if-then rules in its knowledge base and returns:


A diagnosis — the likely cause of the problem
An explanation — the reasoning behind that diagnosis


If no rule matches the exact combination of symptoms, the system falls back to a generic response recommending a professional diagnostic scan.
Example Run
Does the car fail to start? (y/n): y
Do you hear a clicking sound when trying to start? (y/n): y
Are the dashboard/headlights dimmer than usual? (y/n): y
...

------------------------------------------------------------
DIAGNOSIS: Weak or dead battery
------------------------------------------------------------
REASONING: The engine won't start, you hear clicking, and the
lights are dim. This combination points to insufficient power
reaching the starter, which is the classic sign of a weak or
dead battery.
------------------------------------------------------------
Features


Rule-based inference engine using if-then logic
Console-based interactive interface
Diagnosis paired with a clear, human-readable explanation
Graceful handling of invalid input — keeps asking until a valid y/n response is given and never crashes on unexpected input
Easy to extend — new symptoms and rules can be added directly to the knowledge base


How to Run

Option 1: Google Colab


1.Go to colab.research.google.com
2.Create a new notebook and paste the code into a cell
3.Run the cell and answer the prompts as they appear
Tech Used


Python 3
No external libraries — built entirely with core Python


Possible Future Improvements


Expand the knowledge base to cover more vehicle issues
Add a confidence score for diagnoses with partial symptom matches
Build a simple GUI or web interface instead of console-only
Allow multiple diagnoses to be shown when symptoms overlap multiple rules
