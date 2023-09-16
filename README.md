## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)
1. RabbitMQ Server installed and running locally

## Description
1. Square_Data.csv contains info on a square's side length, perimeter, and area.
1. Creates an Emitter that passes square area and perimeter information to two different queues.
1. Area Listener grabs the message from the Area Queue and finds the new Area if the square side length was doubled.
1. Perimeter Listener grabs the message from the Perimeter Queue and finds the new Perimeter if the square side length was doubled.

## Steps
1. Start the Area Listener
2. Start the Perimeter Listener
3. Run the Emitter
4. Close the two Listener Programs

## Screenshot

See a running example with at least 3 concurrent process windows here:

<img align="center" width="921" height="483" src="Emitter.png">
<img align="center" width="921" height="483" src="Area Listener.png">
<img align="center" width="921" height="483" src="Perimeter Listener.png">