from django.db import models
 
def from_500():
    '''
    Returns the next default value for the `ones` field,
    starts from 500
    '''
    # Retrieve a list of `YourModel` instances, sort them by
    # the `ones` field and get the largest entry
    largest = models.objects.all().order_by('ones').last()
    if not largest:
        # largest is `None` if `YourModel` has no instances
        # in which case we return the start value of 500
        return 500
    # If an instance of `YourModel` is returned, we get it's
    # `ones` attribute and increment it by 1
    return largest.ones + 1
 
class Chavespix(models.Model):
    chavepix = models.CharField(primary_key=True, null=False, max_length=100)
    banco = models.CharField(max_length=4, default='')
    conta = models.CharField(max_length=20, default='')
    titular = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'Chavepix:{self.chavepix} | Banco: {self.banco} | Conta: {self.conta} | Titular: {self.titular}'
    
class Enviapix(models.Model):
    idtrans = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    tstrans = models.DateTimeField(auto_now=True, editable=False)
    iptrans = models.CharField(max_length=25, default='127.0.0.1')
    chavepix = models.CharField(max_length=100, null=False)
    banco = models.CharField(max_length=4, blank=True)
    conta = models.CharField(max_length=20, blank=True)
    valor = models.DecimalField(default=1.0, decimal_places=2, max_digits=22)
    titular = models.CharField(max_length=100, blank=True)
    resposta = models.CharField(max_length=500, blank=True)
    minhaconta = models.CharField(max_length=30)
    meunome = models.CharField(max_length=100)


    def __str__(self):
        return None    