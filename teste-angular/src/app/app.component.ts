import { Component, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { MatTable } from '@angular/material/table';


export interface Prod {
  produto: string;
  preco: number;
}




@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  lstProd: Prod[] = Array();
  
  @ViewChild(MatTable)
  tabProd!: MatTable<Prod>;


  displayedColumns: string[] = ['produto', 'preco'];


  onSubmit(form: NgForm){
    let p: Prod = {
      produto: String(form.value.produto),
      preco: Number(form.value.preco) 
    };


    this.lstProd.push(p);
    this.tabProd.renderRows();
    
  }
}
