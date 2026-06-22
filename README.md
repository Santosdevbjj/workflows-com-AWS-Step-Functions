## Formação AWS Cloud Foundations

<img width="105" height="120" alt="1000127839" src="https://github.com/user-attachments/assets/19a72c1f-9f5d-4efc-93db-3fdae64064a0" />



---

# file-validation-workflow


## Fluxo

```
Arquivo Recebido
        |
        ▼
Validate File Lambda
        |
        ▼
Arquivo válido?
   /            \
 Sim            Não
  |               |
  ▼               ▼
Success         Fail 

```

---

## Exemplo de entrada

``` 

{
  "filename": "clientes.csv"
}  


```
---



## Exemplo de saída

```

{
  "filename": "clientes.csv",
  "validationResult": {
    "valid": true
  }
} 



```

---

 
# lambda-execution-workflow



## Fluxo

```
Validate File
      |
      ▼
Process Data
      |
      ▼
Notify Execution
      |
      ▼
Success

```


---


## Fluxo de exceção

```

Validate File
      |
      ▼
Erro?
      |
     Sim
      ▼
Handle Error
      |
      ▼
Fail


```

---


## Exemplo de entrada


```
{
  "filename": "clientes.csv"
}

```

---

## Exemplo de saída


```

{
  "validation": {
    "valid": true
  },
  "processResult": {
    "status": "processed"
  },
  "notification": {
    "status": "notification_sent"
  }
}


```


---


# sns-notification-workflow


## Arquitetura

```

Process Data
      |
      ▼
Publish SNS Event
      |
      ▼
SNS Topic
      |
      ▼
Subscribers
(Lambda, Email, SQS, etc.)


```

---


 # Exemplo de entrada

 ```

{
  "event": "file_processed",
  "filename": "clientes.csv",
  "status": "success"
}


```

---



# Exemplo de mensagem enviada ao SNS

```

{
  "event": "file_processed",
  "filename": "clientes.csv",
  "status": "success"
}

```

---




# Fluxo


```

Process Data
      |
      ▼
Publish Notification
      |
      ▼
SNS Topic
      |
      ▼
Success


```

---


# workflows/sqs-processing-workflow

```

Step Functions
       |
       ▼
Send Message
       |
       ▼
Amazon SQS
       |
       ▼
Consumer Service

```

---




