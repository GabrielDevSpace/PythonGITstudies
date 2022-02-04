from django import forms
from django.core.mail.message import EmailMessage
class ContatoForm(forms.Form):
    name = forms.CharField(label='name')
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Name: {name}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        mail = EmailMessage(
            subject='E-mail Enviado Pelo Sistema!',
            body=conteudo,
            from_email='remetente@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()