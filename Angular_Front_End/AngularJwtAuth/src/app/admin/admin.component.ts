import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { TwitterDataService } from '../services/twitterData.service';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as dasbhboard2 from '../../assets/dist/js/pages/dashboard2.js';
import * as Chart from '../../assets/bower_components/chart.js/Chart.js';

import { AuthService } from '../auth/auth.service';
import { TokenStorageService } from '../auth/token-storage.service';
import { AuthLoginInfo } from '../auth/login-info';

declare var $: any;

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})

@Injectable()
export class AdminComponent implements OnInit {
  board: string;
  errorMessage: string;

  isLoggedIn = false;

  roles: string[] = [];
  private loginInfo: AuthLoginInfo;

  positive_tweets: number = 0;
  negative_tweets: number = 0;
  neutral_tweets: number = 0;
  total_tweets: number = 0;
  positive_tweets_percent: number = 0;
  negative_tweets_percent: number = 0;
  neutral_tweets_percent: number = 0;
  //private averageTweetLength  = [];
  //averageTweetLength: Array<any>;
  averageTweetLength: Object;
  //declare var averageTweetLength;
  twitterData: Array<any>;

  constructor(private authService: AuthService, private tokenStorage: TokenStorageService, private userService: UserService, private twitterDataService: TwitterDataService, private httpClient: HttpClient) { }

  private prediction  = [];
  get_prediction(){
      this.httpClient.get('http://127.0.0.1:5000/api/get/tweets/prediction').subscribe((res : any[])=>{
      this.prediction = res;
      });
  }

  ngOnInit() {

    if (this.tokenStorage.getToken()) {
      this.isLoggedIn = true;
      this.roles = this.tokenStorage.getAuthorities();
    }


    this.userService.getAdminBoard().subscribe(
      data => {
        this.board = data;
      },
      error => {
        this.errorMessage = '${error.status}: ${JSON.parse(error.error).message}';
      }
    );

      // get the average tweet length from Amazon Gateway API GET call using Lambda Function
      this.httpClient.get('http://0.0.0.0:5000/api/get/tweets/statistics').subscribe((res : any)=>{
      this.averageTweetLength = res.average_tweet_length;
      });


    this.twitterDataService.getAll().subscribe(
      data => {
        this.twitterData = data;


        for (let entry of data) {
          if (entry.added_tweet_sentiment == 'positive') {
            this.positive_tweets+=1;
          }
          if (entry.added_tweet_sentiment == 'negative') {
            this.negative_tweets+=1;
          }
          if (entry.added_tweet_sentiment == 'neutral') {
            this.neutral_tweets+=1;
          }
          this.total_tweets = this.positive_tweets + this.negative_tweets + this.neutral_tweets;

          this.neutral_tweets_percent = Math.round(this.neutral_tweets/this.total_tweets*100);
          this.positive_tweets_percent = Math.round(this.positive_tweets/this.total_tweets*100);
          this.negative_tweets_percent = Math.round(this.negative_tweets/this.total_tweets*100);
        }

        this.createPieChart(this.total_tweets,this.positive_tweets,this.negative_tweets,this.neutral_tweets);
      }
    );
    this.loadScript();

  }

   public loadScript() {
      // using set setTimeout to make the search and pagination features work after the angular <tr> data rows
      // are loaded - this might not work with larger data sets!
      setTimeout(function(){
        //do this after view has loaded :)


        // this format (using 'any') to avoid bug with global jquery not including .DataTable()
        // beacause of typescript definition
        ($("#example2") as any).DataTable();
      }, 2000);
  };

// define javascript function for creating a pie chart visualization
public createPieChart(total_tweets,positive_tweets,negative_tweets,neutral_tweets) {

  setTimeout(function(){

//do this after view has loaded :)


//var pieChartCanvas = $('#pieChart').get(0).getContext('2d');

var pieChartCanvas_element = <HTMLCanvasElement> document.getElementById("pieChart");
var pieChartCanvas = pieChartCanvas_element.getContext("2d");

  var pieChart       = new Chart(pieChartCanvas);
  var PieData        = [
    {
      value    : positive_tweets,
      color    : '#00a65a',
      highlight: '#00a65a',
      label    : 'Positive'
    },
    {
      value    : negative_tweets,
      color    : '#dd4b39',
      highlight: '#dd4b39',
      label    : 'Negative'
    },
    {
      value    : neutral_tweets,
      color    : 'rgb(243, 156, 18)',
      highlight: 'rgb(243, 156, 18)',
      label    : 'Neutral'
    },
  ];
  var pieOptions     = {
    // Boolean - Whether we should show a stroke on each segment
    segmentShowStroke    : true,
    // String - The colour of each segment stroke
    segmentStrokeColor   : '#fff',
    // Number - The width of each segment stroke
    segmentStrokeWidth   : 1,
    // Number - The percentage of the chart that we cut out of the middle
    percentageInnerCutout: 50, // This is 0 for Pie charts
    // Number - Amount of animation steps
    animationSteps       : 25,
    // String - Animation easing effect
    animationEasing      : 'easeOutBounce',
    // Boolean - Whether we animate the rotation of the Doughnut
    animateRotate        : true,
    // Boolean - Whether we animate scaling the Doughnut from the centre
    animateScale         : false,
    // Boolean - whether to make the chart responsive to window resizing
    responsive           : true,
    // Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
    maintainAspectRatio  : false,
    // String - A legend template
    legendTemplate       : '<ul class=\'<%=name.toLowerCase()%>-legend\'><% for (var i=0; i<segments.length; i++){%><li><span style=\'background-color:<%=segments[i].fillColor%>\'></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>',
    // String - A tooltip template
    tooltipTemplate      : '<%=value %> <%=label%> tweets'
  };
  // Create pie or douhnut chart
  // You can switch between pie and douhnut using the method below.
  pieChart.Doughnut(PieData, pieOptions);
      }, 1000);
}

}
