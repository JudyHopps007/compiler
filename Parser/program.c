


    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0) {

        return -1;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
       
        return -1;
    }
