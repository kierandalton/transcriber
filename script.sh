docker build -t whisper-test .
docker run -v %cd%:/app -v %cd%:/audio -v %cd%:/output whisper-test