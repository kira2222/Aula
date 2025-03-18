from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from.forms import RegisterForm


# Esta función es llamada cuando el usuario quiere registrarse.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("/")
        else:
            # Si el formulario no es válido, vuelve a renderizar el formulario con errores
            return render(response, "registration/register.html", {"form": form})
    else:
        form = RegisterForm()

        return render(response, "registration/register.html", {"form":form})