import { TutorialService } from './../../services/tutorial.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tutorial-list',
  templateUrl: './tutorial-list.component.html',
  styleUrls: ['./tutorial-list.component.css']
})
export class TutorialListComponent implements OnInit {

  tutorials: any;
  currentTutorial = null;
  currentIndex = -1;
  title = '';

  constructor(private tutorialService: TutorialService) { }

  ngOnInit(): void {
    this.retrieveTutorials();
  }
  
  retrieveTutorials() {
    this.tutorialService.getAll()
    .subscribe(
      data => {
        this.tutorials = data;
        console.log(data);
      },
      error => {
        console.log(error);
      });
  }
  
  refreshList() {
    this.retrieveTutorials();
    this.currentTutorial = null;
    this.currentTutorial = -1;
  }

  setActiveTutorial(tutorial, index) {
    this.currentTutorial = tutorial;
    this.currentIndex = index;
  }

  removeAllTutorials() {
    this.tutorialService.deleteAll()
    .subscribe(
      response => {
        console.log(response);
        this.retrieveTutorials();
      },
      error => {
        console.log(error);
      });
  }

  searchTitle() {
    this.tutorialService.findByTitle(this.title)
    .subscribe(
      data => {
        this.tutorials = data;
        console.log(data);
      },
      error => {
        console.log(error);
      });
  }
}
