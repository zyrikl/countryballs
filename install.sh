detect = grep "Created by Charles Wang" main.py 
if [ $detect -eq  1 ]; then
    python3 ./main.py
else
    echo "Credits not properly installed."
fi
