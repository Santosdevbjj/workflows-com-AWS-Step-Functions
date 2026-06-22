## Formação AWS Cloud Foundations

<img width="105" height="120" alt="1000127839" src="https://github.com/user-attachments/assets/19a72c1f-9f5d-4efc-93db-3fdae64064a0" />



---

## Fluxo

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


---

## Exemplo de entrada

{
  "filename": "clientes.csv"
}  

---



## Exemplo de saída


{
  "filename": "clientes.csv",
  "validationResult": {
    "valid": true
  }
} 


---





