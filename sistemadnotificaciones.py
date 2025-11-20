from abc import ABC, abstractmethod

class notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje, destinatario):
        pass

class email(notificacion):
    def __init__(self, servidor="gmail"):
        self.servidor = servidor
    
    def enviar(self, mensaje, destinatario):
        return f"email enviado a {destinatario}: {mensaje}"

class sms(notificacion):
    def __init__(self, operadora="movistar"):
        self.operadora = operadora
    
    def enviar(self, mensaje, destinatario):
        mensaje_corto = mensaje[:20] + "..." if len(mensaje) > 20 else mensaje
        return f"sms enviado a {destinatario}: {mensaje_corto}"

print(" sistema de notificaciones")
email = email("outlook")
sms = sms("claro")

mensaje = "hola tu pedido ha sido enviado"
print(email.enviar(mensaje, "cliente@email.com"))
print(sms.enviar(mensaje, "3001234567"))
print()