        if 'wikipedia' in query1:
            speak('searching Wikipedia')
            query1=query1.replace("wikipedia","")
            results=wikipedia.summary(query1,sentances=3)
            speak('According to Wikipedia')
            speak (results)
            print(results)
        
        # elif 'open Youtube' in query1:
        #     webbrowser.open("youtube.com")

        elif 'open stack' or 'openstack' in query1:
            webbrowser.open("stackoverflow.com")
        elif 'open git' or 'opengit' in query1:
            webbrowser.open("github.com")
        elif 'open google' in query1:
            webbrowser.open("google.com")
        
        elif 'the time' in query1:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The  time is {strTime}")
