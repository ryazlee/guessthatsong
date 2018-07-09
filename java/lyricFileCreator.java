import java.net.*;
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.applet.Applet;
import java.awt.Graphics;

public class lyricFileCreator {
    public static void main (String[] args){
        String baseSite = "https://www.azlyrics.com/lyrics/#FILLIN#.html";
        String input = args[0] + "/" + args[1];

        String url = searchAndReplace("#FILLIN#", input, baseSite);
        System.out.println(url);        
        
        String data = "";
            
        String baseHTML = readFromFile("../baseHTML.html");
        String eMapping = readFromFile("../emojimapping.txt");   

        try{        
            URL site = new URL(url);        
            
            System.setProperty("http.agent", "Chrome"); 
            
            BufferedReader in = new BufferedReader(new InputStreamReader(site.openStream()));    

            String inputLine;
            while ((inputLine = in.readLine()) != null){
                if (inputLine.equals("      ")) data += "\n";
                else data += inputLine;
            }
            in.close();
        }catch (IOException e){
            System.out.println(e);
        }

            data = data.substring(data.indexOf("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->")+133, data.indexOf("<!-- MxM banner -->") - 14);
            
            String songHTML = updateLyrics(data, eMapping);
            songHTML = songHTML.toLowerCase();
            songHTML = searchAndReplace("#FILLIN#", songHTML, baseHTML);
            writeToFile("../index.html", songHTML);
            
    }
    
    public static void writeToFile(String filename, String content){
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filename))) {
            bw.write(content);
            System.out.println("Done writing to " + filename);

        } catch (IOException e) {
            e.printStackTrace();

        }   
    }  

    public static String readFromFile(String filename){
        String ret = "";
        try{
            List<String> lines = Files.readAllLines(Paths.get(filename));
            for (String line: lines){
                ret += line;
            }
        } catch(IOException e){
            System.out.println(e);
        }

        return ret;
    }
    public static String searchAndReplace(String searchParam, String replacedParam, String base) {
        String newText = base.replaceAll(searchParam, replacedParam);
        return newText;
    }

    public static String updateLyrics(String html, String mapping){
        String ret = html;
        String[] lines = mapping.split("::");
        for (String line: lines){
            String searchparam = line.substring(0, line.indexOf(":"));
            String replaceparam = line.substring(line.indexOf(":")+1, line.indexOf(";"));
            //System.out.println("searching for: " + searchparam + " replacing with: " + replaceparam);
 
            ret = searchAndReplace(searchparam, replaceparam, ret);
        }
        return ret;   
    }

    // Does not work
    public static String removeBracketText(String text){
        int startbracket;
        int endbracket;
        for (int i = 1; i < text.length()-1; i++){
            startbracket = 0;
            endbracket = 0;
            if (text.charAt(i) == '['){
                startbracket = i;
                for (int j = i; j < text.length()-1; j++){
                    if(text.charAt(j) == ']') endbracket = j + 1;
                }
                //System.out.println(startbracket + "     " + endbracket); 
                String searchparam = text.substring(startbracket-1, endbracket+1);
            
                text = searchAndReplace(searchparam, "", text);
            }
        }

        return text;
    }
}
