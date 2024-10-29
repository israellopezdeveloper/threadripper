PYTHON := python3
PIP := $(PYTHON) -m pip
INSTALL_DIR := /opt/threadripper
BIN_DIR := /usr/local/bin
DESKTOP_FILE := /usr/share/applications/threadripper.desktop

# Regla para instalar las dependencias y copiar archivos
install: check-dependencies
	@mkdir -p $(INSTALL_DIR)
	@cp threadripper.py $(INSTALL_DIR)/
	@cp logo.png $(INSTALL_DIR)/
	@chmod 644 $(INSTALL_DIR)/logo.png
	@cp scripts/threadripper.sh $(BIN_DIR)/threadripper
	@chmod +x $(BIN_DIR)/threadripper
	@cp threadripper.desktop $(DESKTOP_FILE)
	@chmod +x $(DESKTOP_FILE)
	@echo "Instalación completa. Ejecuta 'threadripper' para iniciar la aplicación."

# Regla para desinstalar la aplicación
uninstall:
	@rm -rf $(INSTALL_DIR)
	@rm -f $(BIN_DIR)/threadripper
	@rm -f $(DESKTOP_FILE)
	@echo "Desinstalación completa. La aplicación Threadripper ha sido eliminada."

clean:
	@rm -rf __pycache__  *.pyc *.pyo

check-dependencies:
	@$(PIP) install -r requirements.txt > /dev/null

run: check-dependencies
	@streamlit run threadripper.py
