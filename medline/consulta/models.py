from django.db import models
from consulta.models_login import User

# Create your models here.

class Pacientes(User):
    role = models.CharField(max_length=9, default='paciente')
    birth = models.DateField(verbose_name='Data de Nascimento') # formato: 1991-11-15
    cpf = models.CharField(max_length=11, null=True, verbose_name='CPF')

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Medicos(User):
    role = models.CharField(max_length=9, default='medico')
    birth = models.DateField(verbose_name='Data de Nascimento') # formato: 1991-11-15
    cpf = models.CharField(max_length=11, null=True, verbose_name='CPF')
    crm = models.CharField(max_length=20, null=True)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.get_full_name()

    @property
    def imageURL(self):
        try:
            url = self.foto.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class Especialidades(models.Model):
    tipos = [('225105 - Acupuntura','Médico Acumputurista'),
             ('225110 - Alergia e Imunologia','Médico Alergista e Imunologista'),
             ('225151 - Anestesiologia','Médico anestesiologista'),
             ('225115 - Angiologia','Médico angiologista'),
             ('225120 - Cardiologia','Médico Cardiologista'),
             ('225124A - Cardiologia Pediátrica','Médico Cardiologista'),
             ('225210 - Cirurgia Cardiovascular','Médico Cirurgião Cardiovascular'),
             ('225215 - Cirurgia de Cabeça e Pescoço','Médico cirurgião de cabeça e pescoço'),
             ('225295 - Cirurgia de Mão','Médico cirurgião da mão'),
             ('225225 - Cirurgia Geral ','Médico cirurgião geral '),
             ('225230 - Cirurgia Pediátrica','Médico cirurgião pediátrico'),
             ('225235 - Cirurgia Plástica','Médico cirurgião plástico '),
             ('225305 - Citopatologia','Médico citopatologista'),
             ('225125 - Clínica Médica','Médico clínico'),
             ('225280 - Coloproctologia','Médico proctologista'),
             ('225135 - Dermatologia','Médico dermatologista'),
             ('225155 - Endocrinologia e Metabologia','Médico endocrinologista e metabologista'),
             
             ('225310A - Endoscopia digestiva','Médico em endoscopia'),
             ('225310B - Endoscopia respiratoria','Médico em endoscopia'),
             ('225160 - Fisiatria','Médico fisiatra'),
             ('223605 - Fisioterapia','Fisioterapeuta geral'),
             ('223810 - Fonoaudiologia','Fonoaudiólogo'),
             ('225165 - Gastroenterologia','Médico gastroenterologista'),
             ('225175 - Genetica Medica','Médico geneticista'),
             ('225180 - Geriatria','Médico geriatra'),
             ('225250 - Ginecologia e obstetricia','Médico ginecologista e obstetra'),
             ('225185 - Hematologia e hemoterapia','Médico Hematologista'),
             ('225210A - Hemodinamica e Cardiologia Intervencionista','Hemodinamica e Cardiologia Intervencionista'),
             ('225165A - Hepatologia','Hepatologia'),
             ('225195 - Homeopatia','Médico Homeopata'),
             ('225103 - Infectologia','Médico infectologista'),
             ('225255 - Mastologia','Médico Mastologista'),
             ('225315 - Medicina nuclear','Médico em medicina nuclear'),
             ('225170 - Medico Clinico Geral','Médico Generalista'),
             ('225109 - Nefrologia','Médico Nefrologista'),
             ('225124H - Neonatologia','Neonatologia'),
             ('225124I - Neurologia pediatrica','Médico neurologista'),
             ('225260 - Neurocirurgia ','Médico neurocirurgião'),
             ('225112 - Neurologia','Médico neurologista'),

             ('225118 - Nutrologia','Médico nutrologista'),
             ('225265 - Oftalmologia','Médico oftalmologista'),
             ('225121 - Oncologia','Médico oncologista clínico'),
             ('225270 - Ortopedia e traumatologia','Médico ortopedista e traumatologista'),
             ('225275 - Otorrinolaringologia','Médico otorrinolaringologista'),
             ('225335 - Patologia clínica/Medicina laboratorial','Médico patologista clínico /medicina laboratorial'),
             ('225124 - Pediatria','Médico pediatra'),
             ('225127 - Pneumologia','Médico pneumologista'),
             ('251510 - Psicologia','Psicólogo clínico'),
             ('225133 - Psiquiatria','Médico psiquiatra'),
             ('225320 - Radiologia e diagnóstico por imagem','Médico em radiologia e diagnóstico por imagem'),
             ('225330 - Radioterapia','Médico radioterapeuta'),
             ('225136 - Reumatologia','Médico reumatologista'),
             ('223905 - Terapia ocupacional','Terapeuta ocupacional'),
             ('225285 - Urologia','Médico Médico urologista'),
             ('223268 - Cirurgia e traumatologia buco-maxilo-facial','Cirurgião dentista - traumatologista bucomaxilofacial'),
             ('223208 - Dentista clinico geral','Cirurgião dentista - clínico geral'),
             ('223212 - Endodontia','Cirurgião dentista - endodontista'),
             ('223220 - Estomatologia','Cirurgião dentista - estomatologista'),
             ('223224 - Implantodontia','Cirurgião dentista - implantodontista'),
             ('223236 - Odontopediatria','Cirurgião dentista - odontopediatra'),
             ('223240 - Ortodontia','Cirurgião dentista - ortopedista e ortodontista'),

             ('223248 - Periodontia','Cirurgião dentista - periodontista'),
             ('223256 - Protese dentaria','Cirurgião dentista - protesista'),
             ('223260 - Imaginologia odontologica','Imaginologia odontologica'),
             ('225220 - Cirurgia do aparelho digestivo','Médico cirurgião do aparelho digestivo'),
             ('225240 - Cirurgia toracica','Médico cirurgião torácico'),
             ('225124B - Endocrinologia pediatrica','Médico endocrinologista e metabologista'),
             ('223845 - Foniatria','Fonoaudiólogo'),
             ('225124C - Gastroenterologia pediatrica','Médico gastroenterologista'),
             ('225124D - Hematologia e hemoterapia pediatrica','Médico Hematologista'),
             ('225124E - Medicina do adolescente','Medicina do adolescente'),
             ('225150 - Medicina intensiva','Médico em medicina intensiva'),
             ('225124F - Medicina intensiva pediatrica','Médico em medicina intensiva'),
             ('225124G - Nefrologia pediatrica','Médico Nefrologista'),
             ('223710 - Nutricionista','Nutricionista'),
             ('225290 - Oncologia cirurgica','Médico oncologista clínico'),
             ('225122 - Oncologia pediatrica','Médico oncologista clínico'),
             ('225124K - Pneumologia pediatrica','Médico pneumologista'),
             ('225133A - Psiquiatria da infancia eda adolescencia','Psicopedagogo'),
             ('225124L - Reumatologia pediatrica','Médico reumatologista'),
             ('223280 - Dentistica','Dentistica'),
             ('223284 - Disfuncao temporomandibular e dor orafacial.','Cirurgião dentista - disfunção temporomandibular e dor orofacial'),
             ('223228 - Odontogeriatria','Cirurgião dentista - odontogeriatra'),
             
             ('223288 - Odontologia para pacientes com necessidades especiais','Cirurgião dentista - odontologia para pacientes com necessidades especiais'),
             ('223284A - Ortopedia funcional dos maxilares','Ortopedia funcional dos maxilares'),
             ('999999 - Medicamentos Hospitalares','Medicamentos Hospitalares'),
             ('999999A - Opme','Opme'),
             ('225151A - Dor','Dor'),
             ('225112A - Medicina do Sono','Medicina do Sono'),
             ('225203 - Cirurgia Vascular','Médico em cirurgia vascular'),
             ('225310 - Endoscopia','Médico em endoscopia'),
             ('225160A - Medicina Fisica e Reabilitação','Medicina Fisica e Reabilitação'),
             ('225325 - patologia','Médico patologista'),
             ('251605 - Assistente social ','Assistente social '),
             ('223505 - Enfermagem','Técnico de enfermagem'),
             ('999999B - Não Informado','CBO desconhecido ou não informado pelo solicitante'),

            ]
    especialidade = models.CharField(max_length=100, choices=tipos)
    

    def __str__(self):
        return self.especialidade
    
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
    

class Medicos_especialidade(models.Model):
    id_medico = models.ForeignKey(Medicos, on_delete=models.SET_NULL, null=True)
    id_especialidade = models.ForeignKey(Especialidades, on_delete=models.SET_NULL, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    certificado_especialidade = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Médico Por Especialidade'
        verbose_name_plural = 'Médicos Por Especialidade'

class Localidades(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cep = models.CharField(max_length=11, null=True)
    rua = models.CharField(max_length=50, null=True)
    bairro = models.CharField(max_length=50, null=True)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=2, null=True)
    complemento = models.CharField(max_length=30, null=True)


    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Localidade'
        verbose_name_plural = 'Localidades'

class Agendas(models.Model):
    id_medico = models.ForeignKey(Medicos, on_delete=models.SET_NULL, null=True)
    id_especialidade = models.ForeignKey(Especialidades, on_delete=models.SET_NULL, null=True)
    tipos = [('Presencial', 'Presencial'), ('Digital', 'Digital')]
    tipos_consulta = models.CharField(max_length=50, choices=tipos)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

class Compras(models.Model):
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.SET_NULL, null=True)
    data_emissao = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    

    def get_cart_total(self):
        comprasitems = self.compras_consulta_set.all()
        total = sum([item.get_total for item in comprasitems])
        return total

    @property
    def get_cart_items(self):
        comprasitems = self.compras_consulta_set.all()
        total = sum([item.quantity for item in comprasitems])
        return total

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class Compras_consulta(models.Model):
    id_compra = models.ForeignKey(Compras, on_delete=models.SET_NULL, null=True)
    id_medicos_especialidade = models.ForeignKey(Medicos_especialidade, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return str(self.id)


    @property
    def get_total(self):
        total = self.id_medicos_especialidade.preco * self.quantity
        return total

    class Meta:
        verbose_name = 'Consulta Por Compra'
        verbose_name_plural = 'Consultas Por Compra'

