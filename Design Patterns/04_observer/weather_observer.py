class WeatherStation:
    """
    Estação meteorológica que atua como o Subject.
    Monitora mudanças nas condições climáticas e notifica os observadores.
    """
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0
    
    def register_observer(self, observer):
        """Registra um novo observador."""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        """Remove um observador."""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self):
        """Notifica todos os observadores sobre as mudanças climáticas."""
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
    
    def set_measurements(self, temperature, humidity, pressure):
        """Define novas medições e notifica os observadores."""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


class WeatherObserver:
    """Interface para todos os observadores do clima."""
    def update(self, temperature, humidity, pressure):
        """Recebe atualizações da estação meteorológica."""
        pass


class DisplayDevice(WeatherObserver):
    """Dispositivo de exibição que mostra as condições atuais do clima."""
    def __init__(self, name):
        self.name = name
    
    def update(self, temperature, humidity, pressure):
        print(f"{self.name} - Condições Atuais:")
        print(f"Temperatura: {temperature}°C")
        print(f"Umidade: {humidity}%")
        print(f"Pressão: {pressure} hPa")
        print("-" * 30)


class WeatherAlert(WeatherObserver):
    """Sistema de alerta que avisa sobre condições climáticas extremas."""
    def update(self, temperature, humidity, pressure):
        if temperature > 30:
            print("⚠️ ALERTA: Temperatura muito alta! Risco de calor extremo.")
        
        if temperature < 0:
            print("⚠️ ALERTA: Temperatura abaixo de zero! Risco de congelamento.")
        
        if humidity > 90:
            print("⚠️ ALERTA: Umidade muito alta! Possibilidade de chuvas intensas.")


# Exemplo de uso
if __name__ == "__main__":
    # Criando a estação meteorológica (Subject)
    weather_station = WeatherStation()
    
    # Criando os observadores
    phone_display = DisplayDevice("Aplicativo de Clima (Celular)")
    home_display = DisplayDevice("Estação de Clima (Casa)")
    weather_alerts = WeatherAlert()
    
    # Registrando os observadores
    weather_station.register_observer(phone_display)
    weather_station.register_observer(home_display)
    weather_station.register_observer(weather_alerts)
    
    # Simulando mudanças no clima
    print("=== Manhã de Verão ===")
    weather_station.set_measurements(28, 65, 1013)
    
    print("\n=== Tarde de Verão ===")
    weather_station.set_measurements(32, 70, 1010)
    
    # Removendo um observador
    weather_station.remove_observer(home_display)
    
    print("\n=== Noite (após remover o display de casa) ===")
    weather_station.set_measurements(25, 85, 1005)
