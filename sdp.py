class ConfigurationManager:
    _instance = None

    def __new__(cls, config_file_path):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._load_configuration(config_file_path)
        return cls._instance

    def _load_configuration(self, config_file_path):
        """summary
        Args:
            config_file_path (type): description
        """
        self.config = {}
        with open(config_file_path, "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                self.config[key] = value

    def get_setting(self, key):
        return self.config.get(key, None)

config_manager1 = ConfigurationManager("config.txt")
config_manager2 = ConfigurationManager("config.txt")
print("Config Manager 1 Settings:")
print("Host:", config_manager1.get_setting("host"))
print("Port:", config_manager1.get_setting("port"))

print("\nConfig Manager 2 Settings:")
print("Host:", config_manager2.get_setting("host"))
print("Port:", config_manager2.get_setting("port"))

# Config managers are the same instance
print("\nSame Instance:", config_manager1 is config_manager2)
