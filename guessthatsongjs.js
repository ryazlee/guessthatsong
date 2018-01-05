var baseSite = "https://www.azlyrics.com/lyrics/#FILLIN#.html";
var input = "taylorswift/iknewyouweretrouble"
var url = baseSite.replace("#FILLIN#", input)


var baseHTML = "<html><head><meta charset='utf-8'></head><body><link href=\"https://afeld.github.io/emoji-css/emoji.css\" rel=\"stylesheet\"><div style = \"font-family: arial; font-color: white\">#FILLIN#</div></body></html>";

var eMapping = "story:<i class=\"em em-book\"></i>;::phone:<i class=\"em em-telephone_receiver\"></i>;::bad:<i class=\"em em--1\"></i>;::I :<i class=\"em em-eyes\"></i> ;::girl:<i class=\"em em-woman\"></i>;::I':<i class=\"em em-eyes\"></i>';::house:<i class=\"em em-house\"></i>;::House:<i class=\"em em-house\"></i>;::Phone:<i class=\"em em-telephone_receiver\"></i>;::home:<i class=\"em em-house\"></i>;::heart:<i class=\"em em-heart\"></i>;::love:<i class=\"em em-heart\"></i>;::Home:<i class=\"em em-house\"></i>;::bitch:<i class=\"em em-dog\"></i>;::Bitch:<i class=\"em em-dog\"></i>;::Love:<i class=\"em em-heart\"></i>;::Heart:<i class=\"em em-heart\"></i>;:: one: <i class=\"em em-one\"></i>;::One:<i class=\"em em-one\"></i>;::pair:<i class=\"em em-pear\"></i>;::too:<i class=\"em em-v\"></i>;::to:<i class=\"em em-v\"></i>;::two:<i class=\"em em-v\"></i>;::Two:<i class=\"em em-v\"></i>;::baby:<i class=\"em em-baby\"></i>;::Baby:<i class=\"em em-baby\"></i>;::bye:<i class=\"em em-wave\"></i>;::don't:<i class=\"em em-doughnut\"></i>;::Don't:<i class=\"em em-doughnut\"></i>;::Time:<i class=\"em em-clock10\"></i>;::time:<i class=\"em em-clock10\"></i>;::be:<i class=\"em em-honeybee\"></i>;::Be:<i class=\"em em-honeybee\"></i>;::Bee:<i class=\"em em-honeybee\"></i>;::air:<i class=\"em em-dash\"></i>;::star:<i class=\"em em-star\"></i>;::down:<i class=\"em em-arrow_down\"></i>;:: add: <i class=\"em em-heavy_plus_sign\"></i>;::Add:<i class=\"em em-heavy_plus_sign\"></i>;::Down:<i class=\"em em-arrow_down\"></i>;::chicken:<i class=\"em em-chicken\"></i>;::cock:<i class=\"em em-chicken\"></i>;::";


document.write(url);

const cheerio = require("cheerio");


function updateLyrics(html, mapping){
    var ret = html;
    var lines = mapping.split("::");
    for (var line in lines){
        var searchparam = line.substring(0, line.indexOf(":"));
        var replaceparam = line.substring(line.indexOf(":")+1, line.indexOf(";"));
        ret = ret.replace(searchparam, replaceparam);
    }
    return ret;
}

