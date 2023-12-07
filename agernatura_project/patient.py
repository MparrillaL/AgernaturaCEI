import matplotlib.pyplot as plt
import csv



class GenderError(Exception):
    """
    Invalid Gender format. ["M" , "H"]
    """
class ActivityError(Exception):
    """
    Invalid Activity format. ["Sedentario", "Poco activo", "Activo con moderacion", "Activo", "Muy activo"]
    """


class Patient:

    patient_count = 0

    def __init__(self, name, surname, age, gender, height, weight, activity, waist_circunference):

        self.name = name
        self.surname = surname 
        self.age = age
        self.gender = gender.lower()
        if height < 0:
            raise ValueError(f"{height} must be a positive value")
        else:
            self.height = height
        if weight < 0:
            raise ValueError(f"{weight} must be a positive value")
        else:
            self.weight = weight
        self.activity = activity.lower()
        self.waist_circunference = waist_circunference

        if not isinstance(waist_circunference, (int, float)):
            raise TypeError(f"{waist_circunference} must be a float or integer")
        
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string.")
        
        if not isinstance(surname, str):
            raise TypeError(f"{surname} must be a string.")
        
        if not isinstance(age, int):
            raise TypeError(f"{age} must be an integer.")
        
        if gender not in ["h", "m"]:
            raise GenderError(f"{gender} is invalid, must be 'H' for men or 'W' for women.")
        
        if not isinstance(height, (int, float)):
            raise TypeError(f"{height} must be a float or integer")
        
        if not isinstance(weight, (int, float)):
            raise TypeError(f"{weight} must be a float or integer")
        
        if activity not in ["sedentario", "poco activo", "activo con moderacion", "activo con moderación", "activo", "muy activo"]:
            raise ActivityError(f"{activity} invalid, must be in ['Sedentario', 'Poco activo', 'Activo con moderacion', 'Activo', 'Muy activo']")
        
    @classmethod
    def create_patients_from_csv(cls, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            patients = []

            for row in reader:
                cls.patient_count += 1
                patient_id = f"{cls.patient_count:03d}"  

                patient = cls(
                    row['Name'],
                    row['Surname'],
                    int(row['Age']),
                    row['Gender'],
                    float(row['Height']),
                    float(row['Weight']),
                    row['Activity'],
                    float(row['WaistCircumference'])
                )

                patient.patient_id = patient_id
                patients.append(patient)
        return patients
        
    def get_basal_metabolic_rate(self):

        if self.gender == 'm':
            bmr = 655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)
        else:
            bmr = 66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age)
        
        activity_factors = {
        "sedentario": 1.2,
        "poco activo": 1.375,
        "activo con moderacion": 1.55,
        "activo con moderación": 1.55,
        "activo": 1.725,
        "muy activo": 1.9
        }
        
        if self.activity.lower() in activity_factors:
            bmr *= activity_factors[self.activity.lower()]
        print(f"{self.name} {self.surname} necesita {round(bmr, 2)} calorias al día")
        return bmr
paciente1 = Patient("Maria", "Gonzalez", 30, "m", 169, 82, "sedentario", 142)
# paciente1.get_basal_metabolic_rate()


class ScalePatient(Patient):
    def __init__(self, name, surname, age, gender, height, weight, activity, waist_circunference, mgras_percent, bone_mass, muscular_mass_kg, imc, metabolic_age, visceral_gras, water_levels):
        super().__init__(name, surname, age, gender, height, weight, activity, waist_circunference)
        self.mgras_percent = mgras_percent
        self.bone_mass = bone_mass
        self.muscular_mass_kg = muscular_mass_kg
        self.imc = imc
        self.metabolic_age = metabolic_age
        self.visceral_gras = visceral_gras
        self.water_levels = water_levels

        if not isinstance(waist_circunference, (int, float)):
            raise TypeError(f"{waist_circunference} must be a float or integer")
        if waist_circunference < 0:
            raise ValueError(f"{waist_circunference} must be a positive value")

        if not isinstance(mgras_percent, (int, float)):
            raise TypeError(f"{mgras_percent} must be a float or integer")
        if mgras_percent < 0:
            raise ValueError(f"{mgras_percent} must be a positive value")
        
        if not isinstance(bone_mass, (int, float)):
            raise TypeError(f"{bone_mass} must be a float or integer")
        if bone_mass < 0:
            raise ValueError(f"{bone_mass} must be a positive value")
        
        if not isinstance(muscular_mass_kg, (int, float)):
            raise TypeError(f"{muscular_mass_kg} must be a float or integer")
        if muscular_mass_kg < 0:
            raise ValueError(f"{muscular_mass_kg} must be a positive value")
        
        if not isinstance(imc, (int, float)):
            raise TypeError(f"{imc} must be a float or integer")
        if imc < 0:
            raise ValueError(f"{imc} must be a positive value")
        
        if not isinstance(metabolic_age, (int, float)):
            raise TypeError(f"{metabolic_age} must be a float or integer")
        if metabolic_age < 0:
            raise ValueError(f"{metabolic_age} must be a positive value")
        
        if not isinstance(visceral_gras, (int, float)):
            raise TypeError(f"{visceral_gras} must be a float or integer")
        if visceral_gras < 0:
            raise ValueError(f"{visceral_gras} must be a positive value")   
        
    def get_cardiovascular_risk(self):
        if self.gender == 'm':

            if self.waist_circunference < 82:
                cardiovascular_risk = "Normal"
            elif self.waist_circunference >= 82 and self.waist_circunference <= 87:
                cardiovascular_risk = "Elevado"
            else:
                cardiovascular_risk = "Muy elevado"

        else:

            if self.waist_circunference < 95:
                cardiovascular_risk = "Normal"
            elif self.waist_circunference >= 95 and self.waist_circunference <= 101:
                cardiovascular_risk = "Elevado"
            else:
                cardiovascular_risk = "Muy elevado"
                
        return f"Riesgo cardiovascular: {cardiovascular_risk}."
        
    def get_complexion(self):
        if self.gender == 'm':
            if self.height >= 155 and self.height < 159:
                if self.weight < 54:
                    complexion = "pequeña"
                elif self.weight < 59:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 160 and self.height < 164:
                if self.weight < 56:
                    complexion = "pequeña"
                elif self.weight < 61:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 165 and self.height < 169:
                if self.weight < 59:
                    complexion = "pequeña"
                elif self.weight < 64:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 170 and self.height <= 175:
                if self.weight < 65:
                    complexion = "pequeña"
                elif self.weight < 69:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            else:
                complexion = "No se puede determinar la complexión"

        else:
            if self.height >= 170 and self.height < 174:
                if self.weight < 66:
                    complexion = "pequeña"
                elif self.weight < 70:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 175 and self.height < 179:
                if self.weight < 69:
                    complexion = "pequeña"
                elif self.weight < 73:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 180 and self.height < 184:
                if self.weight < 71:
                    complexion = "pequeña"
                elif self.weight < 76:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 185 and self.height <= 190:
                if self.weight < 76:
                    complexion = "pequeña"
                elif self.weight < 85:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            else:
                complexion = "No se puede determinar la complexión"

        return f"su complexion es {complexion}."


        
        
    
    def get_imc_standard(self):
        if self.imc < 18.5:
            imc_standard = "Peso insuficiente"
        elif self.imc >= 18.5 and self.imc < 25:
            imc_standard = "Normopeso"
        elif self.imc >= 25 and self.imc < 27:
            imc_standard = "Sobrepeso grado I"
        elif self.imc >= 27 and self.imc < 30:
            imc_standard = "Sobrepeso grado II (preobesidad)"
        elif self.imc >= 30 and self.imc < 35:
            imc_standard = "Obesidad de tipo I"
        elif self.imc >= 35 and self.imc < 40:
            imc_standard = "Obesidad de tipo II"
        elif self.imc >= 40 and self.imc < 50:
            imc_standard = "Obesidad de tipo III (mórbida)"
        else:
            imc_standard = "Obesidad de tipo IV (extrema)"
        
        return f"Su clasificación segun su IMC es: {imc_standard}."
        
        
    
    def get_mgras_percent(self):
        if self.gender == 'm':
            if self.age <= 20:
                if self.mgras_percent < 16:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 22:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 30:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 25:
                if self.mgras_percent < 18.5:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 25:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 31:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 30:
                if self.mgras_percent < 19:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 25:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 32:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 35:
                if self.mgras_percent < 19:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 25:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 33:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 40:
                if self.mgras_percent < 22:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 28:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 33:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 45:
                if self.mgras_percent < 23:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 28:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 35:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 50:
                if self.mgras_percent < 23:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 29:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 35:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 55:
                if self.mgras_percent < 24:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 30:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 36:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            else:
                if self.mgras_percent < 25:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 31:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 38:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
        else:
            if self.age <= 20:
                if self.mgras_percent < 4:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 14:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 19:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 25:
                if self.mgras_percent < 5:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 14.5:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 22:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 30:
                if self.mgras_percent < 8.5:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 17:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 23:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 35:
                if self.mgras_percent < 9.5:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 18:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 24:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 40:
                if self.mgras_percent < 10.5:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 19:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 25:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 45:
                if self.mgras_percent < 14:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 22:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 27:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 50:
                if self.mgras_percent < 15:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 23:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 28:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            if self.age <= 55:
                if self.mgras_percent < 16:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 24:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 29:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
            else:
                if self.mgras_percent < 17:
                    bodyfat_status = "Delgado"
                elif self.mgras_percent < 25:
                    bodyfat_status = "Ideal"
                elif self.mgras_percent < 31:
                    bodyfat_status = "Promedio"
                else:
                    bodyfat_status = "Superior al promedio"
        
        return f"Su porcentaje de grasa corporal es: {bodyfat_status}."
        
        
    
    def get_w_level(self):
        if self.gender == 'm':
            if 44 <= self.water_levels <= 61:
                w_level = "saludables"
            elif self.water_levels < 44:
                w_level = "inferiores al promedio"
            else:
                w_level = "superiores al promedio"
        else:
            if 49 <= self.water_levels <= 66:
                w_level = "saludables"
            elif self.water_levels < 49:
                w_level = "inferiores al promedio"
            else:
                w_level = "superiores al promedio"
        
        return f"Sus niveles de agua son {w_level}."
        
        
        
    def get_im_muscular(self):
        if self.gender == 'm':
            if self.age <= 30:
                if self.muscular_mass_kg < 35:
                    im_muscular = "Baja"
                elif self.muscular_mass_kg >= 35 and self.muscular_mass_kg <= 41:
                    im_muscular = "Normal"
                else:
                    im_muscular = "Excesiva"
            if self.age <= 60:
                if self.muscular_mass_kg < 33:
                    im_muscular = "Baja"
                elif self.muscular_mass_kg >= 33 and self.muscular_mass_kg <= 38:
                    im_muscular = "Normal"
                else:
                    im_muscular = "Excesiva"
            else:
                if self.muscular_mass_kg < 28:
                    im_muscular = "Baja"
                elif self.muscular_mass_kg >= 28 and self.muscular_mass_kg <= 33:
                    im_muscular = "Normal"
                else:
                    im_muscular = "Excesiva"
        else:
            if self.age <= 30:
                if self.muscular_mass_kg < 43:
                    im_muscular = "Baja"
                elif self.muscular_mass_kg >= 43 and self.muscular_mass_kg <= 56:
                    im_muscular = "Normal"
                else:
                    im_muscular = "Excesiva"
            if self.age <= 60:
                if self.muscular_mass_kg < 40:
                    im_muscular = "Baja"
                elif self.muscular_mass_kg >= 40 and self.muscular_mass_kg <= 50:
                    im_muscular = "Normal"
                else:
                    im_muscular = "Excesiva"
            else:
                if self.muscular_mass_kg < 38:
                    im_muscular = "Baja"
                elif self.muscular_mass_kg >= 38 and self.muscular_mass_kg <= 57:
                    im_muscular = "Normal"
                else:
                    im_muscular = "Excesiva"
        
        return f"Su masa muscular es: {im_muscular}."
        
        
    
    def get_ev_gv(self):
        if self.visceral_gras < 5:
            ev_gv = "Bien"
        elif self.visceral_gras < 9:
            ev_gv = "Medio"
        elif self.visceral_gras < 13:
            ev_gv = "Exceso"
        else:
            ev_gv = "Alarmante"
        
        return f"Su evaluación de grasa visceral es: {ev_gv}."
    

    @classmethod
    def add_patient(cls, patient_obj, waist_circunference, mgras_percent, bone_mass, muscular_mass_kg, imc, metabolic_age, visceral_gras, water_levels):
        name = patient_obj.name
        surname = patient_obj.surname
        age = patient_obj.age
        gender = patient_obj.gender
        height = patient_obj.height
        weight = patient_obj.weight
        activity = patient_obj.activity
        
        new_patient = cls(name,
                          surname,
                          age,
                          gender,
                          height,
                          weight,
                          activity,
                          waist_circunference,
                          mgras_percent,
                          bone_mass,
                          muscular_mass_kg,
                          imc,
                          metabolic_age,
                          visceral_gras,
                          water_levels
                          )
        
        return new_patient
    
    def get_imc_graf(self):
        limites_imc = [0, 18.5, 25, 30, 35, 50, 60]
        colores_imc = ['#E0E0E0', '#7FFF7F', 'yellow', 'orange', '#FF9999', 'red']
        etiquetas_imc = ['Bajo peso', 'Peso normal', 'Sobrepeso', 'Obesidad I', 'Obesidad II',
                 'Obesidad III']

        
        imc_paciente = self.imc
        
        fig, ax = plt.subplots(figsize = (6,3))
        
        for i in range(len(limites_imc) - 1):
            ax.barh(0, limites_imc[i + 1] - limites_imc[i], left=limites_imc[i], height=0.5,
                    color=colores_imc[i], edgecolor='black', label = etiquetas_imc[i])
        
        ax.scatter(imc_paciente, 0, color='white', marker='o', s=50, edgecolor='black')
        ax.text(imc_paciente, 0.18, f'{self.name}', ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xlim(0, 60)
        ax.set_ylim(-1, 1)
        ax.set_xticks([10, 20, 30, 40, 50, 60])
        ax.set_yticks([]) 
        ax.set_xlabel('IMC')
        ax.set_title(f"Barra de IMC: '{self.name} {self.surname}'")
        
        ax.legend(loc = 'upper left', bbox_to_anchor = (1, 1))
        
        plt.tight_layout()
        plt.show()
        
    def get_gc_graf(self):
        limites_gc = [0, 23, 35, 41, 50]
        colores_gc = ["#E0E0E0", "#7FFF7F", "yellow", "#FF9999"]
        etiquetas_gc = ["Bajo grasa", "saludable", "alto grasa", "obeso"]
        gc_paciente = self.mgras_percent        
        fig, ax = plt.subplots(figsize = (6,3))
        
        for i in range(len(limites_gc) - 1):
            ax.barh(0, limites_gc[i + 1] - limites_gc[i], left=limites_gc[i], height=0.5,
                    color=colores_gc[i], edgecolor='black', label = etiquetas_gc[i])
        
        ax.scatter(gc_paciente, 0, color='white', marker='o', s=50, edgecolor='black')
        ax.text(gc_paciente, 0.18, f'{self.name}', ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xlim(0, 50)
        ax.set_ylim(-1, 1)
        ax.set_xticks([10, 20, 30, 40, 50])
        ax.set_yticks([]) 
        ax.set_xlabel(f"% Grasa Corporal")
        ax.set_title(f"% Grasa Corporal: '{self.name} {self.surname}'")
        
        ax.legend(loc = 'upper left', bbox_to_anchor = (1, 1))
        
        plt.tight_layout()
        plt.show()
        
    def get_wl_graf(self):
        limites_wl = [0, 44, 66, 80]
        colores_wl = ["#E0E0E0", "#7FFF7F", "#E0E0E0"]
        etiquetas_wl = ["Bajo", "saludable", "Alto"]
        wl_paciente = self.water_levels       
        fig, ax = plt.subplots(figsize = (6,3))
        
        for i in range(len(limites_wl) - 1):
            ax.barh(0, limites_wl[i + 1] - limites_wl[i], left=limites_wl[i], height=0.5,
                    color=colores_wl[i], edgecolor='black', label = etiquetas_wl[i])
        
        ax.scatter(wl_paciente, 0, color='white', marker='o', s=50, edgecolor='black')
        ax.text(wl_paciente, 0.18, f'{self.name}', ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xlim(30, 80)
        ax.set_ylim(-1, 1)
        ax.set_xticks([30, 45, 50, 60, 65, 80])
        ax.set_yticks([]) 
        ax.set_xlabel(f"% Agua Corporal")
        ax.set_title(f"% Agua Corporal: '{self.name} {self.surname}'")
        
        ax.legend(loc = 'upper left', bbox_to_anchor = (1, 1))
        
        plt.tight_layout()
        plt.show()
        
    def get_cvrisk_graf(self):
        limites_cv = [0, 5, 9, 13, 17, 21]
        colores_cv = ["#7FFF7F", "yellow", "orange", "#FF9999", "red"]
        etiquetas_cv = ["Ninguno", "Aumentado", "Alto", "Muy alto", "Extremo"]
        cv_paciente = self.visceral_gras       
        fig, ax = plt.subplots(figsize = (6,3))
        
        for i in range(len(limites_cv) - 1):
            ax.barh(0, limites_cv[i + 1] - limites_cv[i], left=limites_cv[i], height=0.5,
                    color=colores_cv[i], edgecolor='black', label = etiquetas_cv[i])
        
        ax.scatter(cv_paciente, 0, color='white', marker='o', s=50, edgecolor='black')
        ax.text(cv_paciente, 0.18, f'{self.name}', ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xlim(0, 21)
        ax.set_ylim(-1, 1)
        ax.set_xticks([])
        ax.set_yticks([]) 
        ax.set_xlabel(f"Riesgo Cardiovascular")
        ax.set_title(f"Riesgo Cardiovascular: '{self.name} {self.surname}'")
        
        ax.legend(loc = 'upper left', bbox_to_anchor = (1, 1))
        
        plt.tight_layout()
        plt.show()
    
    def generate_all_graphs(self):
        self.get_imc_graf()
        self.get_gc_graf()
        self.get_wl_graf()
        self.get_cvrisk_graf()
        
def run_health_checks(patient):
    try:
        patient.get_basal_metabolic_rate()
        print("----------------------------------------")
        print(patient.get_cardiovascular_risk())
        print("----------------------------------------")
        print(patient.get_complexion())
        print("----------------------------------------")
        print(patient.get_imc_standard())
        print("----------------------------------------")
        print(patient.get_mgras_percent())
        print("----------------------------------------")
        print(patient.get_w_level())
        print("----------------------------------------")
        print(patient.get_im_muscular())
        print("----------------------------------------")
        print(patient.get_ev_gv())
    except (ValueError, TypeError, GenderError, ActivityError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

paciente1_bascula = ScalePatient.add_patient(paciente1, 142, 35.2, 2.4, 38, 29.5, 52, 12, 42)


# run_health_checks(paciente1_bascula)
# paciente1_bascula.generate_all_graphs()

# paciente1_bascula.get_imc_graf()
# paciente1_bascula.get_gc_graf()
# paciente1_bascula.get_wl_graf()
paciente1_bascula.get_cvrisk_graf()



