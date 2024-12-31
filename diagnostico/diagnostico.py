import random
from experta import KnowledgeEngine, Fact, Rule

class DiagnosticoComputadora(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.sugerencia = ""

    # Reglas para diagnosticar problemas
    @Rule(Fact(problema="pantalla_negra"))
    def problema_pantalla(self):
        sugerencias = [
            "1. Revisa si el cable del monitor está correctamente conectado al puerto de la tarjeta gráfica y al monitor. Si es posible, utiliza un cable diferente para descartar daños.",
            "2. Asegúrate de que el monitor está encendido y que la luz indicadora de energía (LED) está activa.",
            "3. Verifica si el brillo y el contraste del monitor están configurados adecuadamente, ya que configuraciones muy bajas pueden hacer que la pantalla parezca apagada.",
            "4. Intenta reiniciar tanto la computadora como el monitor para descartar problemas temporales de software.",
            "5. Conecta el monitor a otro puerto de video (HDMI, DisplayPort, DVI, VGA) o incluso a otra computadora para descartar problemas con el monitor.",
            "6. Inspecciona el cable y los conectores del monitor en busca de daños visibles, como cortes o pines doblados, y reemplázalos si es necesario.",
            "7. Prueba desconectar y reconectar la tarjeta gráfica en la placa base para asegurarte de que esté bien conectada.",
            "8. Realiza una limpieza interna del gabinete para evitar problemas por polvo en los componentes."
        ]
        self.sugerencia = random.choice(sugerencias)

    @Rule(Fact(problema="sin_conexion_internet"))
    def problema_internet(self):
        sugerencias = [
            "1. Verifica si el módem y el router están encendidos y las luces indicadoras muestran actividad normal. Consulta el manual si las luces indican problemas.",
            "2. Reinicia el módem y el router desconectándolos de la corriente por 30 segundos y volviéndolos a conectar.",
            "3. Asegúrate de que los cables Ethernet entre el módem, el router y la computadora estén firmemente conectados y no tengan daños.",
            "4. Comprueba si la computadora está conectada a la red WiFi correcta y que no haya contraseñas incorrectas almacenadas.",
            "5. Intenta olvidar y reconectar la red WiFi en la configuración para solucionar posibles conflictos de configuración.",
            "6. Prueba si otros dispositivos conectados a la misma red tienen acceso a Internet. Si no lo tienen, el problema podría estar en el proveedor de servicio o en el equipo de red.",
            "7. Realiza un diagnóstico de red desde la configuración de tu sistema operativo.",
            "8. Asegúrate de que el adaptador de red esté habilitado en la configuración de red.",
            "9. Actualiza los drivers del adaptador de red desde el Administrador de Dispositivos."
        ]
        self.sugerencia = random.choice(sugerencias)

    @Rule(Fact(problema="teclado_no_funciona"))
    def problema_teclado(self):
        sugerencias = [
            "1. Asegúrate de que el teclado esté conectado al puerto USB o PS/2 correcto y que esté firmemente asegurado.",
            "2. Prueba conectar el teclado a otro puerto USB en caso de que el puerto actual esté dañado o no funcione correctamente.",
            "3. Verifica en el Administrador de Dispositivos si los drivers del teclado están correctamente instalados o si necesitan actualización.",
            "4. Examina físicamente el teclado para verificar si hay teclas atascadas o residuos que puedan interferir con su funcionamiento.",
            "5. Prueba conectar el teclado a otra computadora para descartar que el problema sea del teclado en sí.",
            "6. Reinicia la computadora y verifica si el teclado responde al ingresar al BIOS o durante el arranque.",
            "7. Realiza una limpieza del teclado utilizando aire comprimido o un paño suave.",
            "8. Comprueba si hay configuraciones de accesibilidad activadas que puedan estar interfiriendo con el uso del teclado."
        ]
        self.sugerencia = random.choice(sugerencias)

    @Rule(Fact(problema="audio_no_funciona"))
    def problema_audio(self):
        sugerencias = [
            "1. Asegúrate de que los altavoces o auriculares estén conectados correctamente al puerto de audio adecuado (verde para altavoces, rosa para micrófono).",
            "2. Verifica si los altavoces están encendidos y que el control de volumen esté configurado a un nivel audible.",
            "3. Comprueba que el volumen de la computadora no esté en silencio o demasiado bajo. Haz clic en el icono de audio en la barra de tareas para confirmarlo.",
            "4. Accede al Administrador de Dispositivos y verifica si los controladores de audio están instalados correctamente o necesitan una actualización.",
            "5. Intenta conectar otros auriculares o altavoces para descartar problemas con el hardware actual.",
            "6. Reinicia la computadora y prueba si el problema de audio persiste. Esto puede resolver conflictos temporales de software.",
            "7. Configura los dispositivos de reproducción predeterminados desde las opciones de sonido en el sistema operativo.",
            "8. Verifica si hay actualizaciones pendientes para el sistema operativo que puedan incluir controladores de audio.",
            "9. Realiza un diagnóstico con la herramienta de resolución de problemas de sonido incluida en tu sistema operativo."
        ]
        self.sugerencia = random.choice(sugerencias)

    @Rule(Fact(problema="lento_rendimiento"))
    def problema_rendimiento(self):
        sugerencias = [
            "1. Cierra programas y ventanas que no estés utilizando para liberar memoria y recursos del sistema.",
            "2. Revisa si hay actualizaciones de software o del sistema operativo pendientes. Las actualizaciones pueden incluir mejoras de rendimiento.",
            "3. Realiza un análisis con un software antivirus o antimalware para descartar infecciones que puedan ralentizar tu computadora.",
            "4. Limpia los archivos temporales y basura utilizando herramientas como el Liberador de Espacio en Disco en Windows o aplicaciones de terceros.",
            "5. Abre el Administrador de Tareas para identificar procesos que consumen muchos recursos. Considera finalizar los procesos no esenciales.",
            "6. Si el rendimiento sigue siendo lento, considera una actualización de hardware, como añadir más memoria RAM o reemplazar el disco duro por un SSD para mejorar la velocidad.",
            "7. Desactiva aplicaciones que se inician automáticamente y que no necesitas.",
            "8. Verifica si el sistema está funcionando en modo de alto rendimiento en la configuración de energía.",
            "9. Limpia físicamente la computadora para evitar sobrecalentamiento debido al polvo en los ventiladores y disipadores de calor.",
            "10. Desfragmenta el disco duro si estás utilizando un HDD en lugar de un SSD."
        ]
        self.sugerencia = random.choice(sugerencias)

    @Rule(Fact(problema="problema_desconocido"))
    def problema_desconocido(self):
        self.sugerencia = "Lo siento, no tengo sugerencias para este problema. Te recomiendo consultar con un técnico especializado o buscar ayuda en línea con una descripción detallada del problema."

    # Método para obtener la sugerencia
    def get_sugerencia(self):
        return self.sugerencia

# Ejemplo de uso
if __name__ == "__main__":
    engine = DiagnosticoComputadora()
    engine.reset()

    # Agregar un problema como hecho
    engine.declare(Fact(problema="pantalla_negra"))
    engine.run()

    print(engine.get_sugerencia())
