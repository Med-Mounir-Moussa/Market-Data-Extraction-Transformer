import { Component, OnInit } from '@angular/core';
import { Website } from '../website' ;

@Component({
  selector: 'app-website-form',
  templateUrl: './website-form.component.html',
  styleUrls: ['./website-form.component.css']
})
export class WebsiteFormComponent implements OnInit {

  constructor() { }
  model = new Website("https://bloomberg.com/markets/currencies",
                    "/html/body/div[5]/main/div/div/div[3]/div[4]/div/table/tbody/tr[1]/td[1]/a/div[2]",
                    "/html/body/div[5]/main/div/div/div[3]/div[4]/div/table/tbody/tr[1]/td[2]");
  submitted = false;
  onSubmit () {this.submitted = true ;}
  ngOnInit() {
  }

}
