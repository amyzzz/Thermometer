public class HelloServlet extends javax.servlet.http.HttpServlet {

    public void doPost(
        javax.servlet.http.HttpServletRequest request,
        javax.servlet.http.HttpServletResponse response)
        throws javax.servlet.ServletException, java.io.IOException {
    }
    public void doGet(
        javax.servlet.http.HttpServletRequest request,
        javax.servlet.http.HttpServletResponse response)
        throws javax.servlet.ServletException, java.io.IOException {
        
        String s = "Hello";


    // get remote user using getUserPrincipal()
    java.security.Principal principal = request.getUserPrincipal();
    String remoteUserName = "";
    if( principal != null )
    remoteUserName = principal.getName();
    // get remote user using getRemoteUser()
    String remoteUser = request.getRemoteUser();

    // check if remote user is granted Mgr role
    boolean isMgr = request.isUserInRole("Mgr");

    // display Hello username for managers and bob. 
    if ( isMgr || remoteUserName.equals("bob") )
    s = "Hello " + remoteUserName;

    String message = "<html> \n" +
    "<head><title>Hello Servlet</title></head>\n" +
    "<body> /n +"
    "<h1> " +s+ </h1>/n " + 
    byte[] bytes = message.getBytes();

    // displays "Hello" for ordinary users 
    // and displays "Hello username" for managers and "bob".
    response.getOutputStream().write(bytes);
    }

}
