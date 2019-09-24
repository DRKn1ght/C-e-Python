//ALUNOS: SERGIO ALVAREZ RA:115735 E GUILHERME PANOBIANCO RA:112679

//DIFICULDADES: trabalhar com strings



#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAXCHAR 1000
int qntaluno = 0;

struct aluno {
 char ra[100];
 char nome[100];
};
struct aluno Alunos[MAXCHAR];


void ler(){
    qntaluno =0;
    FILE *fp;
    char str[MAXCHAR];
    char* filename = "C:/Users/guipa/Desktop/C E PITON/alunos.txt";
    fp = fopen(filename, "r");
    struct aluno alunos;
    if (fp == NULL){
        printf("Nao abre %s",filename);
        return ;
    }
    while (fgets(str, MAXCHAR, fp) != NULL){
        //printf("%s - %i ", str, index);
          if (!strstr(str, "\n"))
        {
            strcat(str, "\n");
            strncpy(alunos.nome, str + 7, strlen(str));
        }else{
        strncpy(alunos.ra, str, 6);
        strncpy(alunos.nome, str + 7, strlen(str));
        Alunos[qntaluno] = alunos;
        qntaluno++;
        }


}
fclose(fp);
}

void buscar(){

    FILE *arquivo;
    arquivo = fopen("C:/Users/guipa/Desktop/C E PITON/alunos.txt","r+");  
    struct aluno alunos;   
    rewind(arquivo);
       
    if (arquivo != NULL){
        char ra[7];
        char str[MAXCHAR];
        int n=0;
        printf("Digite o RA do aluno desejado(Se quiser procurar alunos excluidos digite 000000) ");
        scanf("%s",ra);
        int i = 0;
        while(fgets(str,MAXCHAR,arquivo)!=NULL){
            if (!strcmp(Alunos[i].ra,ra)){
                printf("\nRA    NOME");
                printf("\n%s %s", Alunos[i].ra, Alunos[i].nome);
                n++;
            }
        i++;
        }
        if(n==0){
            printf("\nAluno nao encontrado");
        }            
    }    
    else{
        printf("Arquivo nao encontrado");
    }

    fclose(arquivo);

}

void alterar(){
    ler();
    FILE *arquivo;
    arquivo = fopen("C:/Users/guipa/Desktop/C E PITON/alunos.txt","w");
    
    struct aluno alunos;
    if (arquivo != NULL){

        char ra[7];
        char str[MAXCHAR];
        char nome[100];
        int n=0;
        printf("Digite o RA do aluno que quer alterar o nome ");
        scanf("%s",ra);
        getchar();
        int i = 0;
        char nome1[100];
        printf("Digite o nome do novo aluno ");
        scanf("%[^\n]s",nome1);

         arquivo = fopen("C:/Users/guipa/Desktop/C E PITON/alunos.txt","w");
            for(int index2 = 0; index2 < qntaluno; index2++){
                if (!strcmp(Alunos[index2].ra, ra)){                                    
                    fprintf(arquivo, "%s %s\n", Alunos[index2].ra,  nome1); 
                    strcpy(Alunos[index2].nome, nome1);
                    printf("\nUsuario alterado para %s ", nome1);      
                }
                else{
                    fprintf(arquivo, "%s %s", Alunos[index2].ra, Alunos[index2].nome);
                }   
            }
        }        



        fclose(arquivo);





}



void remover(){

    ler();
    
    FILE *arquivo;
    arquivo = fopen("C:/Users/guipa/Desktop/C E PITON/alunos.txt","w");
    
    struct aluno alunos;
    if (arquivo != NULL){

    char ra[7];
    char str[MAXCHAR];
    char nome[100];
    int n=0;
    printf("Digite o RA do aluno que quer remover ");
    scanf("%s",ra);
    getchar();
    int i = 0;



    arquivo = fopen("C:/Users/guipa/Desktop/C E PITON/alunos.txt","w");
        for(int index2 = 0; index2 < qntaluno; index2++){
            if (!strcmp(Alunos[index2].ra, ra)){   
                strcpy(Alunos[index2].ra, "000000");                                   
                fprintf(arquivo, "%s %s",Alunos[index2].ra,Alunos[index2].nome); 
                
                printf("\nUsuario %s removido ", Alunos[index2].nome);      
            }
            else{
                fprintf(arquivo, "%s %s", Alunos[index2].ra, Alunos[index2].nome);
            }   
        }
    }        



        fclose(arquivo);





}



 void bubble_sort() {
    ler();
    FILE *arquivo;
    arquivo = fopen("relatorio.txt","w+");
    
    struct aluno alunos;
    char temp[MAXCHAR];
    char temp2[MAXCHAR];


    
    for(int i=0;i<=qntaluno;i++)
      for(int j=i+1;j<=qntaluno;j++){
         if(strcmp(Alunos[i].nome,Alunos[j].nome)>0){
            strcpy(temp,Alunos[i].nome);
            strcpy(temp2,Alunos[i].ra) ;           
            strcpy(Alunos[i].nome,Alunos[j].nome);
            strcpy(Alunos[i].ra,Alunos[j].ra);
            strcpy(Alunos[j].nome,temp);
            strcpy(Alunos[j].ra,temp2);

         }
      }
for(int i=0;i<=qntaluno;i++){
    fprintf(arquivo,"%s %s",Alunos[i].ra, Alunos[i].nome);
}
printf("\nArquivo criado com sucesso");
fclose(arquivo);


}






//menu




int main(){
    int i = 0;
    FILE *fp;
    char str[MAXCHAR];
    char* filename = "C:/Users/guipa/Desktop/C E PITON/alunos.txt";
    fp = fopen(filename, "r");
    struct aluno alunos;
    if (fp == NULL){
        printf("Nao abre %s",filename);
        return 1;
    }
    while (fgets(str, MAXCHAR, fp) != NULL){
        //printf("%s - %i ", str, index);
        if (!strstr(str, "\n"))
        {
            strcat(str, "\n");
            strncpy(alunos.nome, str + 7, strlen(str));
        }else{
        strncpy(alunos.ra, str, 6);
        strncpy(alunos.nome, str + 7, strlen(str));
        Alunos[qntaluno] = alunos;
        qntaluno++;
        }
}
    while(i != 5){
        printf("\nDigite a opcao desejada\n");
        printf("OPCAO 1- Buscar aluno por RA \n");
        printf("OPCAO 2- Alterar aluno \n");
        printf("OPCAO 3- Remover aluno \n");
        printf("OPCAO 4- Gerar relatorio \n");
        printf("OPCAO 5- Encerrar o programa \n");
        scanf("%d",&i);

        //switch case
    switch(i){
        case 1:
            
            buscar(i);
        break;    
        case 2:
            ler();
            alterar();
        break;    

        case 3:
            ler();
            remover();
        break;    

        case 4:
            bubble_sort();
        
        break;    


        default:
            printf("\nOpcao nao existe");    
    break;    
    }    

    }    
return 0;

}

