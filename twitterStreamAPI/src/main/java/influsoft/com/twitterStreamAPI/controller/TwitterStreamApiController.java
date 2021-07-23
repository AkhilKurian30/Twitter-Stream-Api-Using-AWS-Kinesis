package influsoft.com.twitterStreamAPI.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping(value = "/twitterstream")
public class TwitterStreamApiController {

    @GetMapping("/test")
    public String getBrandSafetyValues() {

        // TwitterFactory tf = new TwitterFactory(cb.build());
        // Twitter t = tf.getInstance();
        // ResponseList<Status> list = t.getHomeTimeline();
        // for (Status status : list) {
        // System.out.println(status);
        // }
        return "Success";
    }
}
