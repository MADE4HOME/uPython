# Complete project details at https://RandomNerdTutorials.com

from made4home import m4h, PIN_RELAY_1, PIN_IN_1, PIN_RELAY_2, PIN_IN_2, PIN_RELAY_3, PIN_IN_3, PIN_RELAY_4, PIN_IN_4

sck = None

state_on = "ON"
state_off = "OFF"

relay_1_state = state_off
relay_2_state = state_off
relay_3_state = state_off
relay_4_state = state_off

def web_page():
   global relay_1_state, relay_2_state, relay_3_state, relay_4_state, state_off, state_on
   
   page = ""
   
   page += """<html>
   <head>
   """
   
   page += """
     <title>ESP Web Server</title>
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <link rel="icon" href="data:,">
     """
   
   page += """
     <style>
       html {
         font-family: Helvetica;
         display: inline-block;
         margin: 0px auto;
         text-align: center;
       }
   
       h1 {
         color: #0F3376;
         padding: 2vh;
       }
   
       p {
         font-size: 1.5rem;
       }
   
       .button {
         display: inline-block;
         background-color: #e7bd3b;
         border: none;
         border-radius: 4px;
         color: white;
         padding: 16px 40px;
         text-decoration: none;
         font-size: 30px;
         margin: 2px;
         cursor: pointer;
       }
   
       .button2 {
         background-color: #4286f4;
       }
     </style>
     """
   page += """</head><body>"""
   page += """<h1>Made4Home WEB Server</h1>"""

   if m4h.digitalRead(PIN_IN_1) == 0: page += """<p>Input 1: """ + state_on + """</p>"""
   if m4h.digitalRead(PIN_IN_1) == 1: page += """<p>Input 1: """ + state_off + """</p>"""
   if m4h.digitalRead(PIN_IN_2) == 0: page += """<p>Input 2: """ + state_on + """</p>"""
   if m4h.digitalRead(PIN_IN_2) == 1: page += """<p>Input 2: """ + state_off + """</p>"""
   if m4h.digitalRead(PIN_IN_3) == 0: page += """<p>Input 3: """ + state_on + """</p>"""
   if m4h.digitalRead(PIN_IN_3) == 1: page += """<p>Input 3: """ + state_off + """</p>"""
   if m4h.digitalRead(PIN_IN_4) == 0: page += """<p>Input 4: """ + state_on + """</p>"""
   if m4h.digitalRead(PIN_IN_4) == 1: page += """<p>Input 4: """ + state_off + """</p>"""

   page += """<p>Relay 1: <strong>""" + relay_1_state + """</strong></p>"""
   if relay_1_state == state_off:
        page += """<p>
                <a href="/?r1=on">
                    <button class="button">ON</button>
                </a>
                </p>"""
   else:
        page += """<p>
                <a href="/?r1=off">
                    <button class="button button2">OFF</button>
                </a>
                </p>
            """

   page += """<p>Relay 2: <strong>""" + relay_2_state + """</strong></p>"""
   if relay_2_state == state_off:
        page += """<p>
                <a href="/?r2=on">
                    <button class="button">ON</button>
                </a>
                </p>"""
   else:
        page += """<p>
                <a href="/?r2=off">
                    <button class="button button2">OFF</button>
                </a>
                </p>
            """

   page += """<p>Relay 3: <strong>""" + relay_3_state + """</strong></p>"""
   if relay_3_state == state_off:
        page += """<p>
                <a href="/?r3=on">
                    <button class="button">ON</button>
                </a>
                </p>"""
   else:
        page += """<p>
                <a href="/?r3=off">
                    <button class="button button2">OFF</button>
                </a>
                </p>
            """

   page += """<p>Relay 4: <strong>""" + relay_4_state + """</strong></p>"""
   if relay_4_state == state_off:
        page += """<p>
                <a href="/?r4=on">
                    <button class="button">ON</button>
                </a>
                </p>"""
   else:
        page += """<p>
                <a href="/?r4=off">
                    <button class="button button2">OFF</button>
                </a>
                </p>
            """

   page += """
     </body>
     </html>"""

   return page

def setup():
    global sck

    m4h.setup()

    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.bind(('', 80))
    sck.listen(5)

def loop():
    global sck, relay_1_state, relay_2_state, relay_3_state, relay_4_state, state_off, state_on

    conn, addr = sck.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    r1_on = request.find('/?r1=on')
    r1_off = request.find('/?r1=off')
    r2_on = request.find('/?r2=on')
    r2_off = request.find('/?r2=off')
    r3_on = request.find('/?r3=on')
    r3_off = request.find('/?r3=off')
    r4_on = request.find('/?r4=on')
    r4_off = request.find('/?r4=off')

    if r1_on == 6:
        relay_1_state = state_on
        m4h.digitalWrite(PIN_RELAY_1, 1)

    if r1_off == 6:
        relay_1_state = state_off
        m4h.digitalWrite(PIN_RELAY_1, 0)

    if r2_on == 6:
        relay_2_state = state_on
        m4h.digitalWrite(PIN_RELAY_2, 1)

    if r2_off == 6:
        relay_2_state = state_off
        m4h.digitalWrite(PIN_RELAY_2, 0)

    if r3_on == 6:
        relay_3_state = state_on
        m4h.digitalWrite(PIN_RELAY_3, 1)

    if r3_off == 6:
        relay_3_state = state_off
        m4h.digitalWrite(PIN_RELAY_3, 0)

    if r4_on == 6:
        relay_4_state = state_on
        m4h.digitalWrite(PIN_RELAY_4, 1)

    if r4_off == 6:
        relay_4_state = state_off
        m4h.digitalWrite(PIN_RELAY_4, 0)


    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()

def main():

    setup()

    while True:
        loop()
    
if __name__ == "__main__":
    main()
