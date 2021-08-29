package influsoft.com.twitterStreamAPI;

import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.kinesis.producer.Attempt;
import com.amazonaws.services.kinesis.producer.KinesisProducer;
import com.amazonaws.services.kinesis.producer.KinesisProducerConfiguration;
import com.amazonaws.services.kinesis.producer.UserRecordResult;

import org.springframework.boot.autoconfigure.SpringBootApplication;

import twitter4j.FilterQuery;
import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterException;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.conf.ConfigurationBuilder;

@SpringBootApplication
public class TwitterStreamApiApplication {

	public static void main(String[] args) throws TwitterException {

		BasicAWSCredentials cred = new BasicAWSCredentials("", "");
		KinesisProducerConfiguration kpConfig = new KinesisProducerConfiguration()
				.setCredentialsProvider(new AWSStaticCredentialsProvider(cred)).setRegion("us-east-2")
				.setVerifyCertificate(false);
		final KinesisProducer producer = new KinesisProducer(kpConfig);

		String access_token = "";
		String access_token_secret = "";
		String consumer_key = "";
		String consumer_secret = "";

		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(false)
		.setOAuthConsumerKey(consumer_key).setOAuthConsumerSecret(consumer_secret)
				.setOAuthAccessToken(access_token).setOAuthAccessTokenSecret(access_token_secret);

		TwitterStream twitterStream = new TwitterStreamFactory(cb.build()).getInstance();
		StatusListener statusListener = new StatusListener() {

			@Override
			public void onException(Exception ex) {
			}

			@Override
			public void onTrackLimitationNotice(int numberOfLimitedStatuses) {

			}

			@Override
			public void onStatus(Status status) {
				System.out.println("Name => " + status.getUser().getName());
				String strd = status.getUser().getName() + " | " + status.getUser().getLocation() + "\n";
				try {
					ByteBuffer data = ByteBuffer.wrap(strd.getBytes("UTF-8"));
					Future<UserRecordResult> f = producer.addUserRecord("Twitter_Stream_API", "1L", data);
					UserRecordResult result = f.get();
					if (result.isSuccessful()) {
						//System.out.println("shard : " + result.getShardId());
					} else {
						for (Attempt attempt : result.getAttempts()) {
							// failure
						}
					}

				} catch (UnsupportedEncodingException | InterruptedException | ExecutionException e) {
				//	System.out.println
					e.printStackTrace();
				}

			}

			@Override
			public void onStallWarning(StallWarning warning) {

			}

			@Override
			public void onScrubGeo(long userId, long upToStatusId) {

			}

			@Override
			public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) {

			}
		};

		twitterStream.addListener(statusListener);
		String[] tracklist = { "#bigdata"};
		FilterQuery query = new FilterQuery().track(tracklist);
		twitterStream.filter(query);

	}

}
