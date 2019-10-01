package com.nickruta.demo.model;

import org.springframework.data.annotation.Id;


public class Tweet {
	
    @Id
    public String app_id;
    
    public String coordinates;
    public Boolean retweeted;
	public String source;
    public String entities;
    public String reply_count;
    public String favorite_count;
    public String in_reply_to_status_id_str;
    public String geo;
    public String id_str;
    public Long in_reply_to_user_id;
    public String timestamp_ms;
    public Boolean truncated;
    public String text;
    public String retweet_count;
    public String retweeted_status;
    public Long id;
    public String in_reply_to_status_id;
    public String filter_level;
    public String created_at;
    public String place;
    public Boolean favorited;
    public String lang;
    public String contributors;
    public String in_reply_to_screen_name;
    public Boolean is_quote_status;
    public String in_reply_to_user_id_str;
    public String user;
    public String added_tweet_sentiment;
    public String quote_count;
    public String twitter_stream_filter_keyword;
    public String added_tweet_sentiment_positive;
    public String added_tweet_sentiment_negative;
    
	public Tweet(String app_id, String coordinates, Boolean retweeted, String source, String entities,
			String reply_count, String favorite_count, String in_reply_to_status_id_str, String geo, String id_str,
			Long in_reply_to_user_id, String timestamp_ms, Boolean truncated, String text, String retweet_count,
			String retweeted_status, Long id, String in_reply_to_status_id, String filter_level, String created_at,
			String place, Boolean favorited, String lang, String contributors, String in_reply_to_screen_name,
			Boolean is_quote_status, String in_reply_to_user_id_str, String user, String added_tweet_sentiment,
			String quote_count, String twitter_stream_filter_keyword, String added_tweet_sentiment_positive,
			String added_tweet_sentiment_negative) {
		super();
		this.app_id = app_id;
		this.coordinates = coordinates;
		this.retweeted = retweeted;
		this.source = source;
		this.entities = entities;
		this.reply_count = reply_count;
		this.favorite_count = favorite_count;
		this.in_reply_to_status_id_str = in_reply_to_status_id_str;
		this.geo = geo;
		this.id_str = id_str;
		this.in_reply_to_user_id = in_reply_to_user_id;
		this.timestamp_ms = timestamp_ms;
		this.truncated = truncated;
		this.text = text;
		this.retweet_count = retweet_count;
		this.retweeted_status = retweeted_status;
		this.id = id;
		this.in_reply_to_status_id = in_reply_to_status_id;
		this.filter_level = filter_level;
		this.created_at = created_at;
		this.place = place;
		this.favorited = favorited;
		this.lang = lang;
		this.contributors = contributors;
		this.in_reply_to_screen_name = in_reply_to_screen_name;
		this.is_quote_status = is_quote_status;
		this.in_reply_to_user_id_str = in_reply_to_user_id_str;
		this.user = user;
		this.added_tweet_sentiment = added_tweet_sentiment;
		this.quote_count = quote_count;
		this.twitter_stream_filter_keyword = twitter_stream_filter_keyword;
		this.added_tweet_sentiment_positive = added_tweet_sentiment_positive;
		this.added_tweet_sentiment_negative = added_tweet_sentiment_negative;
	}

	@Override
	public String toString() {
		return "Tweets [app_id=" + app_id + ", coordinates=" + coordinates + ", retweeted=" + retweeted + ", source="
				+ source + ", entities=" + entities + ", reply_count=" + reply_count + ", favorite_count="
				+ favorite_count + ", in_reply_to_status_id_str=" + in_reply_to_status_id_str + ", geo=" + geo
				+ ", id_str=" + id_str + ", in_reply_to_user_id=" + in_reply_to_user_id + ", timestamp_ms="
				+ timestamp_ms + ", truncated=" + truncated + ", text=" + text + ", retweet_count=" + retweet_count
				+ ", retweeted_status=" + retweeted_status + ", id=" + id + ", in_reply_to_status_id="
				+ in_reply_to_status_id + ", filter_level=" + filter_level + ", created_at=" + created_at + ", place="
				+ place + ", favorited=" + favorited + ", lang=" + lang + ", contributors=" + contributors
				+ ", in_reply_to_screen_name=" + in_reply_to_screen_name + ", is_quote_status=" + is_quote_status
				+ ", in_reply_to_user_id_str=" + in_reply_to_user_id_str + ", user=" + user + ", added_tweet_sentiment="
				+ added_tweet_sentiment + ", quote_count=" + quote_count + ", twitter_stream_filter_keyword="
				+ twitter_stream_filter_keyword + ", added_tweet_sentiment_positive=" + added_tweet_sentiment_positive
				+ ", added_tweet_sentiment_negative=" + added_tweet_sentiment_negative + "]";
	}
    			
    public Boolean getRetweeted() {
		return retweeted;
	}

	public void setRetweeted(Boolean retweeted) {
		this.retweeted = retweeted;
	}

	public Long getId() {
		return id;
	}
	
	public void setId(Long id) {
		this.id = id;
	}	

}