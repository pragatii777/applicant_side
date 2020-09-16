from django.shortcuts import render,redirect
from io import BytesIO
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.urls import reverse
from accounts.views import get_context

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


my_dict={1:'htmltopdf/resume1.html',2:'htmltopdf/resume2.html'}
#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		if (template.index==1):
			pdf = render_to_pdf(my_dict[fork.design_index], {'dict':get_context(request)})
		else:
			pdf = render_to_pdf(my_dict[fork.design_index], {'dict':manual_resume.context})
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		if (template.index==1):
			pdf = render_to_pdf(my_dict[fork.design_index], {'dict':get_context(request)})
		else:
			pdf = render_to_pdf(my_dict[fork.design_index], {'dict':manual_resume.context})
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "your_resume.pdf"
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response

class fork(View):
	design_index=1
	def get(self,request,temp_index):
		setattr(fork, 'design_index',temp_index)
		return render(request,'htmltopdf/fork.html')


class template(View):
	def get(self,request,from_index):
		setattr(template,'index',from_index)
		return render(request,'htmltopdf/design_sel.html')

class manual_resume(View):
	context={}
	def get(self,request):
		setattr(template,'index',2)
		return render(request,'htmltopdf/index.html')

	def post(self,request):
		dictionary={i:request.POST.get(i) for i in request.POST}
		setattr(manual_resume, 'context',dictionary)
		return render(request,'htmltopdf/design_sel.html')
		#return HttpResponseRedirect('converter/template_sel/2')
