from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import datetime
from .models import *
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection

# Create your views here.
import re


def is_valid_email(email):
    # Regular expression for validating an email
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Match the email against the regex
    if re.match(regex, email):
        return True
    else:
        return False


class Homepage(View):
    def get(self, request):
        year = datetime.now().year
        return render(request, "resume/home.html", {"year": year})


class About(View):
    def get(self, request):
        return render(request, "resume/about.html")


class Contact(View):
    def get(self, request):
        return render(request, "resume/contact.html")

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("mobile")
        plan = request.POST.get("plan")
        message = request.POST.get("message")
        if len(name) == 0:
            return HttpResponse("Please Enter a Valid Name", status=400)
        if len(email) == 0:
            return HttpResponse("Please Enter a Valid Email", status=400)

        if len(message) == 0:
            return HttpResponse("Please Write a Message", status=400)
        if len(phone) > 0:
            if not (phone.isdigit()):
                return HttpResponse("Contact Number is not Valid", status=400)
        if not (is_valid_email(email)):
            return HttpResponse("Please Enter a Valid Email", status=400)

        contact = ContactModel(
            name=name, message=message, phone=phone, email=email, plan=plan
        )

        contact.save()
        i = 1
        connection = get_connection()

        if i == 1:
            email = EmailMultiAlternatives(
                subject=f"{name} dropped a message.",
                body=f"{name} \n\n {email} \n\n {phone} \n\n has filled the form and chose {plan}.\n\n Kindly contact.",
                from_email=settings.EMAIL_HOST_USER,
                to=["gdsr786@gmail.com"],
                connection=connection,
            )

            email.send()
            i += 1
            connection.close()
        return HttpResponse("Success", status=200)
        # except Exception as e:
        #     print(e)
        #     return HttpResponse("Something Went Wrong.", status=400)


class SubscribeView(View):
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        if len(name) == 0 or len(email) == 0:
            return HttpResponse("Please Fill the required fields", status=400)
        if not (is_valid_email(email)):
            return HttpResponse("Please enter a valid email.", status=400)
        else:
            newsletter = NewsLetterModel(name=name, email=email)
            newsletter.save()
            return HttpResponse("Success", status=200)


class BlogsView(View):
    def get(self, request):
        all_blogs = BlogModel.objects.all()
        return render(request, "resume/blogs.html", {"blogs": all_blogs})


class BlogDetailsView(View):
    def get(self, request, url):
        blog = BlogModel.objects.get(url=url)
        all_blogs = BlogModel.objects.all()
        comments = CommentModel.objects.filter(blog=blog)
        tags = blog.tags.split(",")
        context = {
            "blog": blog,
            "comments": comments,
            "all_blogs": all_blogs,
            "tags": tags,
        }
        return render(request, "resume/blog_details.html", context)

    def post(self, request, url):
        name = request.POST.get("name")
        email = request.POST.get("email")
        blog1 = request.POST.get("blog")
        comment = request.POST.get("comment")
        if len(name) == 0 or len(email) == 0 or len(comment) == 0:
            return HttpResponse("Please Fill the required fields", status=400)
        if not (is_valid_email(email)):
            return HttpResponse("Please Enter a Valid Email.", status=400)
        if CommentModel.objects.filter(email=email, blog=blog1).exists():
            return HttpResponse(
                "Your Comment already exists for this blog.", status=400
            )
        else:
            blog = BlogModel.objects.get(id=blog1)
            # Get the current date and format it
            current_date = datetime.now().strftime("%Y-%m-%d")
            comment = CommentModel(
                name=name, email=email, blog=blog, comment=comment, date=current_date
            )
            comment.save()
            return HttpResponse("Success", status=200)
