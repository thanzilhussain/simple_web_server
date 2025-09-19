# EX01 Developing a Simple Webserver

# Date:19/09/2008
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 20px;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        .layer {
            background: white;
            margin: 15px auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            width: 80%;
        }
        .layer h2 {
            color: #16a085;
        }
        ul {
            list-style-type: square;
        }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>

    <div class="layer">
        <h2>Application Layer</h2>
        <ul>
            <li>HTTP (Hypertext Transfer Protocol)</li>
            <li>HTTPS (HTTP Secure)</li>
            <li>FTP (File Transfer Protocol)</li>
            <li>SMTP (Simple Mail Transfer Protocol)</li>
            <li>POP3 (Post Office Protocol v3)</li>
            <li>IMAP (Internet Message Access Protocol)</li>
            <li>DNS (Domain Name System)</li>
            <li>SNMP (Simple Network Management Protocol)</li>
        </ul>
    </div>

    <div class="layer">
        <h2>Transport Layer</h2>
        <ul>
            <li>TCP (Transmission Control Protocol)</li>
            <li>UDP (User Datagram Protocol)</li>
        </ul>
    </div>

    <div class="layer">
        <h2>Internet Layer</h2>
        <ul>
            <li>IP (Internet Protocol)</li>
            <li>ICMP (Internet Control Message Protocol)</li>
            <li>ARP (Address Resolution Protocol)</li>
            <li>RARP (Reverse Address Resolution Protocol)</li>
        </ul>
    </div>

    <div class="layer">
        <h2>Network Access Layer</h2>
        <ul>
            <li>Ethernet</li>
            <li>Wi-Fi (IEEE 802.11)</li>
            <li>PPP (Point-to-Point Protocol)</li>
            <li>Frame Relay</li>
        </ul>
    </div>

</body>
</html>

# OUTPUT:
![alt text](<Screenshot 2025-09-19 170002.png>)
![alt text](<Screenshot 2025-09-19 174508.png>)

# RESULT:
The program for implementing simple webserver is executed successfully.
