import { Component, OnInit } from '@angular/core';
import { Website } from '../website' ;
import { FormGroup,FormBuilder,Validators } from '../../../node_modules/@angular/forms';
import { WebsiteFormService } from '../services/website-form.service';

@Component({
  selector: 'app-website-form',
  templateUrl: './website-form.component.html',
  styleUrls: ['./website-form.component.css']
})
export class WebsiteFormComponent implements OnInit {
  
  webForm : FormGroup;
  submitted = false;
  constructor(private formBuilder: FormBuilder, private webService:WebsiteFormService ) { }
  model = new Website("https://www.dailyfx.com/forex-rates",
             "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]/span/a",
             "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]/span")
 
  onSubmit() {
    
    this.submitted = true ; 
    const formValue = this.webForm.value;
    const newWebsite = new Website(
      formValue['url'],
      formValue['productXPATH'], 
      formValue['valueXPATH']
    );
    console.log(newWebsite.url);
    console.log(newWebsite.productXPATH);
    this.webService.putInDataBase(newWebsite.url,newWebsite.productXPATH,newWebsite.valueXPATH).subscribe();
    this.webService.getDataBase().subscribe();
  }

  ngOnInit() {
    this.initForm();
  }

  initForm() {
    this.webForm = this.formBuilder.group({
      url: ['', Validators.required],
      productXPATH: ['', Validators.required],
      valueXPATH: ['', Validators.required]
      }); 
  }

}

