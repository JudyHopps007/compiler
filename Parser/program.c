
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0)

serv_addr.sin_family = AF_INET;
 serv_addr.sin_port = htons(PORT);